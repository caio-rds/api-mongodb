import os
from dotenv import load_dotenv

load_dotenv('app/.env')

databases = {
    'mongo_db': os.getenv('MONGO_URI')
}