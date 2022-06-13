from app.database.mongodb import Database

class MdbInterface:
    def __init__(self):
        self.db = Database()

    async def get(self, data):
        get_db = await self.db.get(
            database=data.database,
            collection=data.collection,
            query=data.query,
            opt_list=data.opt_list
        )

        return get_db
