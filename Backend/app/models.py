from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Users(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    phone: str


class Roles(BaseModel):
    id: int
    name: str
    user: str
    description: str


        
