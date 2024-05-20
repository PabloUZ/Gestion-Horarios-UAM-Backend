from typing import List
from src.api.courses.schemas.group import Group
from src.api.courses.models.group import Group as GroupModel
from sqlalchemy.orm import Session

class GroupRepository():    
    def __init__(self, db) -> None:        
        self.db: Session = db
    
    def get_all_groups(self) -> List[Group]: 
        query = self.db.query(GroupModel)
        return query.all()
    
    def get_group_by_id(self, id: int ):
        element = self.db.query(GroupModel).filter(GroupModel.id == id).first()    
        return element
    
    def get_groups_by_course_and_number(self, course_code: str, number: int) -> Group | None:
        element = self.db.query(GroupModel).filter(GroupModel.course_code == course_code, GroupModel.number == number).first()
        return element

    def delete_group(self, id: int ) -> dict: 
        element: Group= self.db.query(GroupModel).filter(GroupModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_group(self, group:Group ) -> Group:
        new_group = GroupModel(**group.model_dump())    
        self.db.add(new_group)
        self.db.commit()    
        self.db.refresh(new_group)
        return new_group
    
    def update_group(self, id: int, group: Group) -> dict:        
        element = self.db.query(GroupModel).filter(GroupModel.id == id).first()                
        element.name = group.name
        element.number = group.number     
        self.db.commit()        
        self.db.refresh(element)        
        return element