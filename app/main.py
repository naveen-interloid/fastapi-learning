from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.book_router import router as book_router
from app.routers.user_router import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(book_router)


@app.get('/')
def home():
    return {
        'message':'Welcome to ORM'
    }