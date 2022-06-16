from fastapi import APIRouter
from app.endpoints.mongodb import mdb_routes

router = APIRouter()


router.include_router(mdb_routes.router, prefix='/mongodb', tags=['MongoDB'])


@router.get('/health')
async def health():
    return {'DB Python API': 'OK'}
