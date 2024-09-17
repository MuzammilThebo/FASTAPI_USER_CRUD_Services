from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class UserInDB(UserBase):
    active: bool

    class Config:
        orm_mode = True
