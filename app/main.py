from fastapi import FastAPI
from api import auth, books, util_ops
from core.errors import (
    http_exception_handler,
    book_not_found_handler,
    duplicate_book_handler,
    auth_error_handler,
    permission_error_handler
)
from domain.exceptions import (
    BookNotFoundError,
    DuplicateBookError,
    AuthenticationError,
    AuthorizationError
)
from core.logging_middleware import LoggingMiddleware

def create_app() -> FastAPI:
    app = FastAPI(title="Backend Training API")

    # Middleware
    app.add_middleware(LoggingMiddleware)

    # Routers
    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(books.router, prefix="/books", tags=["books"])
    app.include_router(util_ops.router, prefix="/utils", tags=["utils"])

    # Exception handlers
    app.add_exception_handler(BookNotFoundError, book_not_found_handler)
    app.add_exception_handler(DuplicateBookError, duplicate_book_handler)
    app.add_exception_handler(AuthenticationError, auth_error_handler)
    app.add_exception_handler(AuthorizationError, permission_error_handler)

    return app

app = create_app()
