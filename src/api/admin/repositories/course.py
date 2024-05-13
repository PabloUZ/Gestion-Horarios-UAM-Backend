from src.api.courses.schemas.course import Course
from src.api.courses.repositories.course import CourseRepository 



class CourseRepository:
    def __init__(self, db):
        self.db = db

    def add_courses(self, courses: dict):
        for course in courses.values():
            self.add_course(course)


    def add_course(self, course: dict):
        pass