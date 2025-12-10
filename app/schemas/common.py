from pydantic import BaseModel
from typing import List, Generic, TypeVar

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    page: int
    size: int
    total: int
