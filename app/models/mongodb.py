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
    data: dict
    insert_one: Optional[bool]


class Put(BaseModel):
    database: str
    collection: str
    values: dict
    where: dict
    update_one: Optional[bool]


class Delete(BaseModel):
    database: str
    collection: str
    query: dict
    delete_one: Optional[bool]