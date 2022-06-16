from typing import Optional
from pydantic import BaseModel


class Get(BaseModel):
    database: str
    collection: str
    query: dict
    options: Optional[dict]


class Post(BaseModel):
    database: str
    collection: str
    document: dict


class Put(BaseModel):
    database: str
    collection: str
    values: dict
    where: dict
    upsert: Optional[bool] = False


class Delete(BaseModel):
    database: str
    collection: str
    query: dict