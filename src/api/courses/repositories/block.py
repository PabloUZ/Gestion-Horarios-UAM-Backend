from typing import List
from src.api.courses.schemas.block import Block
from src.api.courses.models.block import Block as BlockModel
from sqlalchemy import func

class BlockRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_blocks(self) -> List[Block]: 
        query = self.db.query(BlockModel)
        return query.all()
    
    def get_block_by_id(self, id: int ):
        element = self.db.query(BlockModel).filter(BlockModel.id == id).first()    
        return element

    def delete_block(self, id: int ) -> dict: 
        element: Block= self.db.query(BlockModel).filter(BlockModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_block(self, block:Block ) -> dict:
        new_block = BlockModel(**block.model_dump())    
        self.db.add(new_block)
        self.db.commit()    
        self.db.refresh(new_block)
        return new_block
    
    def update_block(self, id: int, block: Block) -> dict:        
        element = self.db.query(BlockModel).filter(BlockModel.id == id).first()                
        element.name = block.name          
        self.db.commit()        
        self.db.refresh(element)        
        return element
