from src.api.courses.schemas.course import Course
from src.api.courses.repositories.course import CourseRepository

from src.api.courses.schemas.group import Group
from src.api.courses.repositories.group import GroupRepository

from src.api.courses.schemas.professor import Professor
from src.api.courses.repositories.professor import ProfessorRepository

from src.api.courses.schemas.classtime import Classtime
from src.api.courses.repositories.classtime import ClasstimeRepository

from src.api.courses.schemas.room import Room
from src.api.courses.repositories.room import RoomRepository

from fastapi.encoders import jsonable_encoder


class CourseAdminRepository:
    def __init__(self, db):
        self.db = db

    def add_courses(self, courses: dict):
        for course in courses.values():
            self.add_course(course)

    def add_course(self, course: dict):

        result = CourseRepository(self.db).get_course_by_code(course['code'])
        if not result:
            CourseRepository(self.db).create_new_course(
                Course(code=course['code'], name=course['name'], credits=None, type_id=None))

        for group in course['groups']:
            self.add_group(course['code'], group)

    def add_group(self, course_code: str, group: dict):

        
        
        proffesor_id = None
        if group['proffesor']:
            proffesor_id = self.add_proffesor(group['proffesor'])

        result = GroupRepository(self.db).get_group_by_number_and_course(number=group['number'], course_code=course_code)
        group_id = None
        if not result:
            group_model = GroupRepository(self.db).create_new_group(Group(
            name=group['name'], number=group['number'], proffesor_id=proffesor_id, course_code=course_code))
            group_id = jsonable_encoder(group_model)['id']
        else:
            group_id = jsonable_encoder(result)['id']

        for classtime in group['classtimes']:
            self.add_classtime(classtime, group_id)

    def add_proffesor(self, proffesor_name: str) -> int:
        # Buscar si ya existe el profesor
        result = ProfessorRepository(
            self.db).get_professor_by_name(proffesor_name)
        if result:
            return jsonable_encoder(result)['id']

        # Crearlo en caso de que no exista
        result = ProfessorRepository(self.db).create_new_professor(
            Professor(name=proffesor_name))
        return jsonable_encoder(result)['id']

    def add_classtime(self, classtime: dict, group_id: int):
        room_id = None
        if classtime['room']:
            room_id = self.add_room(classtime['room'])

        ClasstimeRepository(self.db).create_new_classtime(Classtime(day=classtime['day'], start_hour=classtime['start_hour'], start_minute=classtime[
            'start_minute'], end_hour=classtime['end_hour'], end_minute=classtime['end_minute'], group_id=group_id, room_id=room_id))

    def add_room(self, room_name: str) -> int:
        # Buscar si ya existe el salón
        result = RoomRepository(self.db).get_room_by_name(room_name)
        if result:
            return jsonable_encoder(result)['id']

        # Obtener el bloque al que pertenece el aula
        block_id = self.get_block(room_name)

        # Crearlo en caso de que no exista
        result = RoomRepository(self.db).create_new_room(
            Room(name=room_name, block_id=block_id))
        return jsonable_encoder(result)['id']

    def get_block(self, room_name: str) -> int:
        room = room_name.split()
        if len(room) > 1:
            if self.is_fundadores(room):
                return 1
            if self.is_sacatin(room):
                return 2
            if self.is_bavaria(room):
                return 3
            if self.is_fisioterapia(room):
                return 4
            if self.is_lab(room):
                if room_name in laboratorios: return laboratorios[room_name]
        return None

    def is_fundadores(self, room: str) -> bool:
        if room[1] == 'F':
            return True
        if room[1].startswith('F'):
            return True
        return False

    def is_sacatin(self, room: str) -> bool:
        if room[1] == '16':
            return True
        return False

    def is_bavaria(self, room: str) -> bool:
        if room[0].startswith('19'):
            return True
        return False

    def is_fisioterapia(self, room: str) -> bool:
        if room[1] == '13':
            return True
        return False

    def is_lab(self, room: str) -> bool:
        if room[0] == 'LABORATORIO':
            return True
        return False


laboratorios = {
    'LABORATORIO DE OCLUS': 2,
    'LABORATORIO DE OCLUSION': 2,
    'LABORATORIO KINESIOT': 4,
    'LABORATORIO DE RESTA': 2,
    'LABORATORIO DE RESTAURA': 2,
    'LABORATORIO RESTAURA': 2,
    'LABORATORIO ELECTRON': 2,
    'LABORATORIO DE CONFE': 2,
    'LABORATORIO FISICA 1': 2,
    'LABORATORIO FISICA 2': 2,
    'LABORATORIO FISICA 3': 2,
    'LABORATORIO DE REDES': 2,
    'LABORATORIO DE SIMUL': 4,
    'LABORATORIO SIMULACI': 4,
    'LABORATORIO PROCESO': 2,
    'LABORATORIO MANTENIM': 2,
    'LABORATORIO 1 (FLUID': 2,
    'LABORATORIO TEJEDURI': 2,
    'LABORATORIO TEXTIL': 2,
}
