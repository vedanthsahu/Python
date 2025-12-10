from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str]
    created_at: datetime
