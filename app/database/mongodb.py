from fastapi import HTTPException

from app.cfg.dotenvs import databases
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(databases.get('mongo_db'))

    async def get(self, database: str, collection: str, query: dict, opt_list:dict = None, find_one: bool = False):
        if opt_list is None:
            opt_list = {'_id': 0}
        try:
            if find_one:
                result = self.client[database][collection].find_one(query, opt_list)
                return result
            else:
                result = self.client[database][collection].find(query, opt_list)
                return list(result)
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def post(self, database: str, collection: str, data: dict, insert_one: bool = False):
        try:
            if insert_one:
                result = self.client[database][collection].insert_one(data)
                return result.acknowledged
            else:
                result = self.client[database][collection].insert_many(data)
                return result.acknowledged
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)


    async def put(self, database: str, collection: str, where: dict, values: dict, update_one: bool = False):
        try:
            if update_one:
                result = self.client[database][collection].update_one(where, {"$set": values}, upsert=True)
                return result.modified_count
            else:
                result = self.client[database][collection].update_many(where, {"$set": values}, upsert=True)
                return result.modified_count
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)


    async def delete(self, database: str, collection: str, query: dict, delete_one: bool = False):
        try:
            if delete_one:
                result = self.client[database][collection].delete_one(query)
                return result.deleted_count
            else:
                result = self.client[database][collection].delete_many(query)
                return result.deleted_count
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)
