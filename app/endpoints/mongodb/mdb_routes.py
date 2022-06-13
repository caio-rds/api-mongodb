from fastapi import APIRouter
from app.models.mongodb import *
from app.controller.mongodb import MdbInterface

router = APIRouter()
mdb_interface = MdbInterface()

@router.get('/')
async def get_mongodb(payload: Get):
    return await mdb_interface.get(payload)

@router.post('/')
async def post_mongodb():
    return {'message': 'Hello World'}

@router.put('/')
async def put_mongodb():
    return {'message': 'Hello World'}

@router.delete('/')
async def delete_mongodb():
    return {'message': 'Hello World'}