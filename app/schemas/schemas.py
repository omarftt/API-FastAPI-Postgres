from typing import List, Optional, Generic,TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class UserSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    lastname: Optional[str]=None
    email: str

    class Config:
        orm_mode = True

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class Response (GenericModel,Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]=None