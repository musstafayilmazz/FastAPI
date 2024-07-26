from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from storeapi.logging_conf import configure_logging
from storeapi.database import database
from storeapi.routers.post import router as post_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


app.include_router(post_router)
