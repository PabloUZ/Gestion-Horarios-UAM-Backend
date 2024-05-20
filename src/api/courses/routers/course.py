from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.course import Course
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.course import CourseRepository

course_router = APIRouter(prefix='/courses', tags=['courses'])

#CRUD courses

@course_router.get('',response_model=List[Course],description="Returns all courses")
def get_courses()-> List[Course]:
    db= SessionLocal()
    result = CourseRepository(db).get_all_courses()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@course_router.get('/{id}',response_model=Course,description="Returns data of one specific course")
def get_courses(id: int = Path(ge=1)) -> Course:
    db = SessionLocal()
    element=  CourseRepository(db).get_course_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested course was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@course_router.post('',response_model=dict,description="Creates a new course")
def create_categorie(course: Course = Body()) -> dict:
    db= SessionLocal()
    new_course = CourseRepository(db).create_new_course(course)
    return JSONResponse(
        content={        
        "message": "The course was successfully created",        
        "data": jsonable_encoder(new_course)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@course_router.delete('/{id}',response_model=dict,description="Removes specific course")
def remove_courses(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CourseRepository(db).get_course_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested course was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    CourseRepository(db).delete_course(id)  
    return JSONResponse(
        content={        
            "message": "The course was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@course_router.put('/{id}', tags=['courses'], response_model=dict, description="Updates the data of specific course") 
def update_course(id: int = Path(ge=1), course: Course = Body()) -> dict:    
    db = SessionLocal()    
    element = CourseRepository(db).get_course_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested course was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = CourseRepository(db).update_course(id, course)    
    return JSONResponse(
                content={        
                    "message": "The course was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )