from app.database.mongodb import Database


class MdbController:
    def __init__(self):
        self.db = Database()

    async def get(self, data):
        get_db = await self.db.get(
            database=data.database,
            collection=data.collection,
            query=data.query,
            opt_list=data.opt_list,
            find_one=data.find_one
        )

        return get_db

    async def post(self, data):
        post_db = await self.db.post(
            database=data.database,
            collection=data.collection,
            data=data.data,
            insert_one=data.insert_one
        )

        if post_db:
            return {'inserted': True}
        return {'inserted': False}

    async def put(self, data):
        put_db = await self.db.put(
            database=data.database,
            collection=data.collection,
            where=data.where,
            values=data.values,
            update_one=data.update_one
        )

        return {'modified_count': put_db}

    async def delete(self, data):
        delete_db = await self.db.delete(
            database=data.database,
            collection=data.collection,
            query=data.query,
            delete_one=data.delete_one
        )

        return {'deleted_count': delete_db}
