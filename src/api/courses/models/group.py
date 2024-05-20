from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100))
    number = Column(String(length=6))
    course_code = Column(String(length=8), ForeignKey('courses.code'), nullable=False)
    proffesor_id = Column(Integer, ForeignKey('proffesors.id'), nullable=True)

    professor = relationship("Professor", back_populates="groups")
    classtimes = relationship("Classtime", back_populates="group")
    course = relationship("Course", back_populates="groups")
