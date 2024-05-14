from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def get_courses(self) -> list:
        pass