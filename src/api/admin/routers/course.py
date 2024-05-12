from fastapi import APIRouter
from src.scrapping.administrator import Administrator
from fastapi.responses import JSONResponse
router = APIRouter(prefix='/admin/courses')

admin = Administrator()

@router.post('')
def generate_courses():
    admin.generate_courses()
    
    return JSONResponse(content="Bien", status_code=201)