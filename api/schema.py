from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int

    class Config:
        orm_mode = True