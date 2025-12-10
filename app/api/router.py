from fastapi import APIRouter
from api import auth, books

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(books.router, prefix="/books", tags=["Books"])
