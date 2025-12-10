import asyncio
from datetime import datetime
from typing import List, Optional

from domain.models import Book
from domain.exceptions import BookNotFoundError, DuplicateBookError


class BookRepository:
    """
    Repository for handling book storage.
    Uses in-memory list for now.
    """

    def __init__(self):
        self._books: List[Book] = []
        self._next_id = 1

    # --------------------------
    # CREATE
    # --------------------------

    async def create(self, title: str, author: str, description: Optional[str]) -> Book:
        await asyncio.sleep(0)  # simulate async DB

        # Prevent duplicates
        for b in self._books:
            if b.title == title and b.author == author:
                raise DuplicateBookError("Book already exists.")

        book = Book(
            id=self._next_id,
            title=title,
            author=author,
            description=description,
            created_at=datetime.utcnow()
        )

        self._books.append(book)
        self._next_id += 1

        return book

    # --------------------------
    # READ / GET
    # --------------------------

    async def get(self, book_id: int) -> Book:
        await asyncio.sleep(0)

        for book in self._books:
            if book.id == book_id:
                return book

        raise BookNotFoundError(f"Book with ID {book_id} not found")

    async def list(self, skip: int, limit: int) -> List[Book]:
        await asyncio.sleep(0)
        return self._books[skip: skip + limit]

    async def count(self) -> int:
        await asyncio.sleep(0)
        return len(self._books)

    # --------------------------
    # UPDATE
    # --------------------------

    async def update(self, book_id: int, **fields) -> Book:
        await asyncio.sleep(0)

        book = await self.get(book_id)

        for field, value in fields.items():
            if value is not None:
                setattr(book, field, value)

        return book

    # --------------------------
    # DELETE
    # --------------------------

    async def delete(self, book_id: int) -> None:
        await asyncio.sleep(0)

        book = await self.get(book_id)
        self._books.remove(book)
