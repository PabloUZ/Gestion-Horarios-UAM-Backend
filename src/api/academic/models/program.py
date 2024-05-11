from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class Program(Base):
    __tablename__ = "program"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=False)
    study_plan = relationship("StudyPlan", back_populates="programs")
    faculty = relationship("Faculty", back_populates="programs")