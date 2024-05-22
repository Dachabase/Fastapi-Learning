from  pydantic import BaseModel

class Staff(BaseModel):
    name : str
    age : int
    staffID : int
    email : str
    gender  : str