from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    cc: str = Field(min_length=6, max_length=12, pattern=r'^\d*$')
    email: str = Field(min_length=6, max_length=80, pattern=r'^[a-z0-9!&\-#.~]+@[a-z0-9]+\.(([a-z0-9]+\.)+)?[a-z0-9]+$')
    first_name: str = Field(min_length=1, max_length=50, pattern=r'^[A-Za-z\s]+$')
    last_name: str = Field(min_length=1, max_length=50, pattern=r'^[A-Za-z\s]+$')
    password: str = Field(min_length=8, max_length=30)
    active: bool = Field()

class UpdateUser(BaseModel):
    email: str = Field(min_length=6, max_length=80, pattern=r'^[a-z0-9!&\-#.~]+@[a-z0-9]+\.(([a-z0-9]+\.)+)?[a-z0-9]+$')
    first_name: str = Field(min_length=1, max_length=50, pattern=r'^[A-Za-z\s]+$')
    last_name: str = Field(min_length=1, max_length=50, pattern=r'^[A-Za-z\s]+$')
    active: bool = Field()

class ChangePassword(BaseModel):
    password: str = Field(min_length=8, max_length=30)
