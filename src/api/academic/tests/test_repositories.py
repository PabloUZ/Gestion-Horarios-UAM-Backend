
from src.api.academic.repositories.faculty import FacultyRepository
from src.api.config.database import SessionLocal
import pytest

def create_faculty():
    db = SessionLocal()
    faculty = {
        "name": "Faculty of Engineering"
    }
    res = FacultyRepository(db).create_faculty(faculty)
    print(res)
    assert res.name == "Faculty of Engineering"
    
def good_get_faculties():
    db = SessionLocal()
    res = FacultyRepository(db).get_faculties(None, None)
    print(res)
    assert len(res) > 0
    
def bad_get_faculties():
    db = SessionLocal()
    res = FacultyRepository(db).get_faculties(None, None)
    print(res)
    assert len(res) == 0
    
def good_get_faculty():
    db = SessionLocal()
    res = FacultyRepository(db).get_faculty(1)
    print(res)
    assert res.name == "Faculty of Engineering"
    
def bad_get_faculty():
    db = SessionLocal()
    res = FacultyRepository(db).get_faculty(1)
    print(res)
    assert res is None
    
def update_faculty():
    db = SessionLocal()
    res = FacultyRepository(db).update_faculty(1, {"name":"Faculty of Science"})
    print(res)
    assert res.name == "Faculty of Science"
    
def good_delete_faculty():
    db = SessionLocal()
    res = FacultyRepository(db).delete_faculty(1)
    print(res)
    assert res.name == "Faculty of Science"

def bad_delete_faculty():
    db = SessionLocal()
    res = FacultyRepository(db).delete_faculty(4)
    print(res)
    assert res.name == "Faculty of Science"