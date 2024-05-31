from fastapi import FastAPI

from api import api_router
from utils import engine, Base

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

async def startup():
    async with engine.begin() as conn:
        print("migration service start...")
        # await conn.run_sync(Base.metadata.drop_all) # drop all table 
        await conn.run_sync(Base.metadata.create_all) # create table on database

        print("migration done..")

app.add_event_handler("startup", startup)

        