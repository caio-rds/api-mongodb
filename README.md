# Routes

### Get
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "query": {"user_id": 93},
    "options": {"_id": 0, "name": 1},
    "find_one": True
#### }

return data (if not find_one will return a list)

### POST
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "data": {"user_id": 93},    
    "insert_one": True
#### }

return inserted_docs number

### PUT
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "where": {"user_id": 93},
    "values": {"user_id": 93, "name": "teste"},
    "update_one": True
#### }

return updated_docs number

### DELETE
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "query": {"user_id": 93},
    "delete_one": True
#### }

return deleted_docs number