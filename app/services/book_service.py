from fastapi import Depends
from typing import Optional

from repositories.book_repo import BookRepository
from domain.exceptions import BookNotFoundError, DuplicateBookError
from schemas.common import PaginatedResponse
from schemas.book import BookResponse


class BookService:
    """
    Handles business logic for books.
    """

    def __init__(self, repo: BookRepository = Depends()):
        self.repo = repo

    # --------------------------
    # CREATE
    # --------------------------

    async def create_book(self, title: str, author: str, description: Optional[str]):
        try:
            book = await self.repo.create(title, author, description)
            return BookResponse(**book.__dict__)
        except DuplicateBookError:
            raise

    # --------------------------
    # GET / DETAILS
    # --------------------------

    async def get_book(self, book_id: int) -> BookResponse:
        try:
            book = await self.repo.get(book_id)
            return BookResponse(**book.__dict__)
        except BookNotFoundError:
            raise

    # --------------------------
    # LIST / PAGINATION
    # --------------------------

    async def list_books(self, page: int, size: int):
        skip = (page - 1) * size

        books = await self.repo.list(skip, size)
        total = await self.repo.count()

        return PaginatedResponse[BookResponse](
            items=[BookResponse(**b.__dict__) for b in books],
            page=page,
            size=size,
            total=total,
        )

    # --------------------------
    # UPDATE
    # --------------------------

    async def update_book(self, book_id: int, title: Optional[str], author: Optional[str], description: Optional[str]):
        try:
            updated = await self.repo.update(
                book_id,
                title=title,
                author=author,
                description=description
            )

            return BookResponse(**updated.__dict__)

        except BookNotFoundError:
            raise

    # --------------------------
    # DELETE
    # --------------------------

    async def delete_book(self, book_id: int):
        try:
            await self.repo.delete(book_id)
        except BookNotFoundError:
            raise
