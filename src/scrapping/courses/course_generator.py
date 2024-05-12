from .course import Course

class CourseGenerator:
    def __init__(self, course):
        self.course: Course = course

    def generate(self) -> list:
        course_list = self.course.get_courses()
        if course_list:
            return course_list
