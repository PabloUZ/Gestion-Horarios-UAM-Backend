from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=60))
    number = Column(Integer)
    course_code = Column(String(length=4), ForeignKey('courses.code'), nullable=False)
    proffesor_id = Column(Integer, ForeignKey('proffesors.id'), nullable=True)

    professor = relationship("Professor", back_populates="groups")
    classtime = relationship("Classtime", back_populates="group")
    course = relationship("Course", back_populates="groups")
