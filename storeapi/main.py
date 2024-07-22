from fastapi import FastAPI
from storeapi.routers.post import router as posts_router

app = FastAPI()
app.include_router(posts_router, tags=["posts"])


@app.get("/")
async def root():
    return {"message": "Hello, World"}
