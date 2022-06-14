from fastapi import APIRouter
from app.models.mongodb import *
from app.controller.mongodb import MdbController

router = APIRouter()
mdb_interface = MdbController()


@router.get('/')
async def get_mongodb(payload: Get):
    return await mdb_interface.get_one(payload)


@router.get('/many')
async def get_many_mongodb(payload: Get):
    return await mdb_interface.get_many(payload)


@router.post('/')
async def post_mongodb(payload: Post):
    return await mdb_interface.post_one(payload)


@router.post('/many')
async def post_many_mongodb(payload: Post):
    return await mdb_interface.post_one(payload)


@router.put('/')
async def put_mongodb(payload: Put):
    return await mdb_interface.put_one(payload)


@router.put('/many')
async def put_many_mongodb(payload: Put):
    return await mdb_interface.put_many(payload)


@router.delete('/')
async def delete_mongodb(payload: Delete):
    return await mdb_interface.delete_one(payload)


@router.delete('/many')
async def delete_many_mongodb(payload: Delete):
    return await mdb_interface.delete_many(payload)
