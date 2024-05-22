from fastapi import APIRouter, Depends, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.block import Block
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.block import BlockRepository
from src.api.middlewares.has_permission import HasPermission
from src.api.middlewares.has_access import has_access

blocks_router = APIRouter(prefix='/blocks', tags=['blocks'])

#CRUD blocks

@blocks_router.get('',response_model=List[Block],description="Returns all blocks" )
def get_blocks()-> List[Block]:
    db= SessionLocal()
    result = BlockRepository(db).get_all_blocks()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@blocks_router.get('/{id}',response_model=Block,description="Returns data of one specific block")
def get_blocks(id: int = Path(ge=1)) -> Block:
    db = SessionLocal()
    element=  BlockRepository(db).get_block_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested block was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@blocks_router.post('',response_model=dict,description="Creates a new block", dependencies=[Depends(has_access), Depends(HasPermission("CREATE_BLOCK"))])
def create_block(block: Block = Body()) -> dict:
    db= SessionLocal()
    new_block = BlockRepository(db).create_new_block(block)
    return JSONResponse(
        content={        
        "message": "The block was successfully created",        
        "data": jsonable_encoder(new_block)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@blocks_router.delete('/{id}',response_model=dict,description="Removes specific block", dependencies=[Depends(has_access), Depends(HasPermission("DELETE_BLOCK"))])
def remove_blocks(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = BlockRepository(db).get_block_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested block was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    BlockRepository(db).delete_block(id)  
    return JSONResponse(
        content={        
            "message": "The block was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@blocks_router.put('/{id}', tags=['blocks'], response_model=dict, description="Updates the data of specific block", dependencies=[Depends(has_access), Depends(HasPermission("UPDATE_BLOCK"))]) 
def update_block(id: int = Path(ge=1), block: Block = Body()) -> dict:    
    db = SessionLocal()    
    element = BlockRepository(db).get_block_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested block was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = BlockRepository(db).update_block(id, block)    
    return JSONResponse(
                content={        
                    "message": "The block was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )
