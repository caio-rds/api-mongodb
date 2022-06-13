from fastapi import APIRouter
from app.models.mongodb import *
from app.controller.mongodb import MdbController

router = APIRouter()
mdb_interface = MdbController()

@router.get('/')
async def get_mongodb(payload: Get):
    return await mdb_interface.get(payload)

@router.post('/')
async def post_mongodb(payload: Post):
    return await mdb_interface.post(payload)

@router.put('/')
async def put_mongodb(payload: Put):
    return await mdb_interface.put(payload)

@router.delete('/')
async def delete_mongodb(payload: Delete):
    return await mdb_interface.delete(payload)
