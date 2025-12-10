from fastapi import APIRouter, Depends, HTTPException, status

from schemas.book import (
    BookCreate,
    BookUpdate,
    BookResponse,
)
from schemas.common import PaginatedResponse

from services.book_service import BookService
from domain.exceptions import BookNotFoundError, DuplicateBookError
from api.auth import get_current_user


router = APIRouter()


# --------------------------
# CREATE BOOK
# --------------------------

@router.post("/", response_model=BookResponse)
async def create_book(
    body: BookCreate,
    svc: BookService = Depends(),
    user=Depends(get_current_user)  # auth-protected
):

    try:
        return await svc.create_book(
            title=body.title,
            author=body.author,
            description=body.description
        )

    except DuplicateBookError as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )


# --------------------------
# GET BOOK BY ID
# --------------------------

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int,
    svc: BookService = Depends(),
    user=Depends(get_current_user)
):
    try:
        return await svc.get_book(book_id)

    except BookNotFoundError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex)
        )


# --------------------------
# LIST BOOKS (PAGINATION)
# --------------------------

@router.get("/", response_model=PaginatedResponse[BookResponse])
async def list_books(
    page: int = 1,
    size: int = 10,
    svc: BookService = Depends(),
    user=Depends(get_current_user)
):
    return await svc.list_books(page=page, size=size)


# --------------------------
# UPDATE BOOK
# --------------------------

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int,
    body: BookUpdate,
    svc: BookService = Depends(),
    user=Depends(get_current_user)
):
    try:
        return await svc.update_book(
            book_id=book_id,
            title=body.title,
            author=body.author,
            description=body.description
        )

    except BookNotFoundError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex)
        )


# --------------------------
# DELETE BOOK
# --------------------------

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: int,
    svc: BookService = Depends(),
    user=Depends(get_current_user)
):
    try:
        await svc.delete_book(book_id)

    except BookNotFoundError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex)
        )

    return None
