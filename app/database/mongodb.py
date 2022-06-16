from fastapi import HTTPException

from app.cfg.dotenvs import databases
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(databases.get('mongo_db'))

    async def find_one(self, database: str, collection: str, query: dict, options: dict = None):
        try:
            if not options:
                options = {'_id': 0}
            result = self.client[database][collection].find_one(query, options)
            return result
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def find(self, database: str, collection: str, query: dict, options: dict = None):
        try:
            if not options:
                options = {'_id': 0}
            result = self.client[database][collection].find(query, options)
            return list(result)
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def insert_one(self, database: str, collection: str, document: dict):
        try:
            result = self.client[database][collection].insert_one(document)
            return result.acknowledged
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def insert_many(self, database: str, collection: str, document: dict):
        try:
            result = self.client[database][collection].insert_many(document)
            return result.acknowledged
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def update_one(self, database: str, collection: str, where: dict, values: dict, upsert: bool):
        try:
            result = self.client[database][collection].update_one(where, {"$set": values}, upsert=upsert)
            return result.modified_count
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def update_many(self, database: str, collection: str, where: dict, values: dict, upsert: bool):
        try:
            result = self.client[database][collection].update_many(where, {"$set": values}, upsert=upsert)
            return result.modified_count
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def delete_one(self, database: str, collection: str, query: dict):
        try:
            result = self.client[database][collection].delete_one(query)
            return result.deleted_count
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def delete_many(self, database: str, collection: str, query: dict):
        try:
            result = self.client[database][collection].delete_many(query)
            return result.deleted_count
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)
