from .course_generator import CourseGenerator
from .course_saver import CourseSaver
from .course_processor import CourseProcessor

class CourseFachade:
    def __init__(self, course):
        self.course_generator = CourseGenerator(course)
        self.course_saver = CourseSaver()
        self.course_processor = CourseProcessor()

    def generate_courses(self) -> dict:
        raw_courses = self.course_generator.generate()
        self.course_processor.set_courses(raw_courses)
        courses = self.course_processor.process()
        self.course_saver.save(courses)
        return courses
        