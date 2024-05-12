from .course_generator import CourseGenerator
from .course_saver import CourseSaver

class CourseFachade:
    def __init__(self, course):
        self.course_generator = CourseGenerator(course)
        self.course_saver = CourseSaver()

    def generate_courses(self):
        courses = self.course_generator.generate()
        print(courses)
        try:
            self.course_saver.save(courses)
        except Exception as e:
            print('Hubo un error')
        