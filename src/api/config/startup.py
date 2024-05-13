
from src.api.config.database import SessionLocal 
from src.api.courses.repositories.block import BlockRepository
from src.api.courses.schemas.block import Block

from src.api.courses.repositories.course_type import CourseTypeRepository
from src.api.courses.schemas.course_type import CourseType



class Startup:
    def __init__(self):
        self.db= SessionLocal()
    
    def add_blocks(self):
        print('ADDING BLOCKS')
        result = BlockRepository(self.db).create_new_block(Block(name='EDIFICIO FUNDADORES', prefix='F'))
        print(f'Added: {result}')
        result = BlockRepository(self.db).create_new_block(Block(name='EDIFICIO SACATÍN', prefix='16'))
        print(f'Added: {result}')
        result = BlockRepository(self.db).create_new_block(Block(name='EDIFICIO BAVARIA', prefix='19'))
        print(f'Added: {result}')
        result = BlockRepository(self.db).create_new_block(Block(name='EDIFICIO FISIOTERAPIA', prefix='13'))
        print(f'Added: {result}')

    def add_course_types(self):
        print('ADDING COURSE TYPES')
        result = CourseTypeRepository(self.db).create_new_courseType(CourseType(name='MICROCURRICULAR'))
        print(f'Added: {result}')
        result = CourseTypeRepository(self.db).create_new_courseType(CourseType(name='MESOCURRICULAR'))
        print(f'Added: {result}')
        result = CourseTypeRepository(self.db).create_new_courseType(CourseType(name='MACROCURRICULAR'))
        print(f'Added: {result}')

    


