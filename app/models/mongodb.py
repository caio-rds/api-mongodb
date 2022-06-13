from typing import Optional
from pydantic import BaseModel


class Get(BaseModel):
    database: str
    collection: str
    find_one: Optional[bool]
    query: dict
    opt_list: Optional[dict]


class Post(BaseModel):
    database: str
    collection: str
    query: dict

class Put(BaseModel):
    database: str
    collection: str
    update_one: Optional[bool]
    query: dict
    opt_list: Optional[dict]

class Delete(BaseModel):
    database: str
    collection: str
    query: dict