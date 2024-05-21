from src.api.courses.repositories.course import CourseRepository 
from src.api.courses.schemas.course import Course

def test_get_all_courses():
    assert CourseRepository.get_all_courses() != None

def test_get_all_courses():
    assert CourseRepository.get_course_by_code("1") != None

def test_get_all_courses():
    assert CourseRepository.delete_course(1) != None

def test_get_all_courses(course:Course):
    assert CourseRepository.create_new_course(course) != None

def test_get_all_courses(course:Course):
    assert CourseRepository.update_course(1, course) != None

