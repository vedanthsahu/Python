from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.errors import ServerErrorMiddleware
from fastapi import status

from domain.exceptions import (
    AuthenticationError,
    AuthorizationError,
    BookNotFoundError,
    DuplicateBookError,
)


def create_error_payload(message: str, code: int):
    return {
        "error": {
            "message": message,
            "status_code": code
        }
    }


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=create_error_payload(exc.detail, exc.status_code)
    )


async def book_not_found_handler(request: Request, exc: BookNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=create_error_payload(str(exc), status.HTTP_404_NOT_FOUND)
    )


async def duplicate_book_handler(request: Request, exc: DuplicateBookError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=create_error_payload(str(exc), status.HTTP_400_BAD_REQUEST)
    )


async def auth_error_handler(request: Request, exc: AuthenticationError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=create_error_payload(str(exc), status.HTTP_401_UNAUTHORIZED)
    )


async def permission_error_handler(request: Request, exc: AuthorizationError):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=create_error_payload(str(exc), status.HTTP_403_FORBIDDEN)
    )
