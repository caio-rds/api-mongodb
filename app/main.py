from fastapi import FastAPI
from app.endpoints.router import router

app = FastAPI(
    title='Databases FastAPI',
    description='Integration with Databases',
    version='0.0.1',
    contact={
        'name': 'Caio Reis',
        'url': 'https://github.com/caio-rds',
        'email': 'caiodtn@gmail.com'
    },
    license_info={
        'name': 'Copyrights GTS 2022'
    }
)

app.include_router(router, prefix='/db')
