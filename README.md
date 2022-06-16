# Routes

### Get
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "query": {"user_id": 93},
    "options": {"_id": 0, "name": 1}
#### }

return data (if not find_one will return a list)

### POST
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "document": {"user_id": 93}
#### }

return inserted_docs number

### PUT
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "where": {"user_id": 93},
    "values": {"user_id": 93, "name": "teste"}
#### }

return updated_docs number

### DELETE
http://127.0.0.1:8000/db/mongodb/
#### {
    "database": "fivem",
    "collection": "outfit",    
    "query": {"user_id": 93}
#### }

return deleted_docs number