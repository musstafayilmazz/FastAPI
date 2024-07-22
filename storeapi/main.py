from fastapi import FastAPI
from contextlib import asynccontextmanager
from storeapi.routers.post import router as posts_router
from storeapi.database import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(posts_router, tags=["posts"])


@app.get("/")
async def root():
    return {"message": "Hello, World"}
