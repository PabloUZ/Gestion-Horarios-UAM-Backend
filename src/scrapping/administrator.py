
from .courses.course_fachade import CourseFachade

from .courses.course_scrapping import CourseScrapping
from .courses.course_database import CourseDatabase


class Administrator:
    def __init__(self):
        # Constantes
        self.SCRAPPING = 0
        self.DATABASE = 1
        self.USER = 2

        self.course_option = self.SCRAPPING
        self.academic_option = self.SCRAPPING

        self.year = 2024
        self.period = 1

        self.course = self.__get_course_instance()

        self.course_fachade = CourseFachade(self.course)

        


    def __get_course_instance(self):
        if self.course_option == self.SCRAPPING:
            return CourseScrapping(self.year, self.period)

        if self.course_option == self.DATABASE:
            return CourseDatabase()
    
    def __get_academic_instance(self):
        pass
    

    def generate_courses(self) -> dict:
        return self.course_fachade.generate_courses()
    
    def set_scrapping_period(self, year, period):
        self.year = year
        self.period = period
        