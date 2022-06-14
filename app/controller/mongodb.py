from fastapi.encoders import jsonable_encoder

from app.database.mongodb import Database


class MdbController:
    def __init__(self):
        self.db = Database()

    async def get_one(self, data):
        get_db = await self.db.find_one(
            database=data.database,
            collection=data.collection,
            query=data.query
        )
        return jsonable_encoder(get_db)

    async def get_many(self, data):
        get_db = await self.db.find(
            database=data.database,
            collection=data.collection,
            query=data.query
        )
        return jsonable_encoder(get_db)

    async def post_one(self, data):
        post_db = await self.db.insert_one(
            database=data.database,
            collection=data.collection,
            data=data.data
        )

        if post_db:
            return jsonable_encoder({'inserted': True})
        return jsonable_encoder({'inserted': False})

    async def post_many(self, data):
        post_db = await self.db.insert_many(
            database=data.database,
            collection=data.collection,
            data=data.data
        )

        if post_db:
            return jsonable_encoder({'inserted': True})
        return jsonable_encoder({'inserted': False})

    async def put_one(self, data):
        put_db = await self.db.update_one(
            database=data.database,
            collection=data.collection,
            where=data.where,
            values=data.values,
            upsert=data.upsert
        )

        return jsonable_encoder({'modified_count': put_db})

    async def put_many(self, data):
        put_db = await self.db.update_many(
            database=data.database,
            collection=data.collection,
            where=data.where,
            values=data.values
        )

        return jsonable_encoder({'modified_count': put_db})

    async def delete_one(self, data):
        delete_db = await self.db.delete_one(
            database=data.database,
            collection=data.collection,
            query=data.query
        )

        return jsonable_encoder({'deleted_count': delete_db})

    async def delete_many(self, data):
        delete_db = await self.db.delete_many(
            database=data.database,
            collection=data.collection,
            query=data.query
        )

        return jsonable_encoder({'deleted_count': delete_db})
