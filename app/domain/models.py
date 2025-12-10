from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# --------------------------
# USER MODEL
# --------------------------
class User(BaseModel):
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "extra": "forbid"  # forbid unknown fields
    }

# --------------------------
# BOOK MODEL (if not already present)
# --------------------------
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "extra": "forbid"
    }
