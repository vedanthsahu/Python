from typing import Optional
from domain.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    """
    Simple in-memory user storage.
    """
    def __init__(self):
        self.users: dict[str, User] = {}  # key=email

    async def create_user(self, email: str, password: str) -> User:
        if email in self.users:
            raise ValueError("User already exists")
        hashed = pwd_context.hash(password)
        user = User(email=email, hashed_password=hashed)
        self.users[email] = user
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        return self.users.get(email)

    async def verify_user(self, email: str, password: str) -> bool:
        user = await self.get_user_by_email(email)
        if not user:
            return False
        return pwd_context.verify(password, user.hashed_password)
import asyncio

# Create a test user
async def create_test_user(repo):
    await repo.create_user("test@example.com", "password123")

# Only run if this file is executed directly
if __name__ == "__main__":
    repo = UserRepository()
    asyncio.run(create_test_user(repo))
    print("Test user created!")
