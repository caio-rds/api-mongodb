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
                #print(list(result))
                return list(result)
        except Exception:
            raise HTTPException(detail='Exception Happened', status_code=500)

    async def post(self, data):
        pass

    async def put(self, data):
        pass

    async def delete(self, data):
        pass
    