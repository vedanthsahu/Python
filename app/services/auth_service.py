from fastapi import Depends
from core.security import (
    create_access_token,
    verify_password,
    decode_access_token,
)
from domain.exceptions import AuthenticationError
from schemas.auth import UserIdentity
from repositories.user_repo import UserRepository


class AuthService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    # --------------------------
    # LOGIN
    # --------------------------

    async def login(self, username: str, password: str) -> str:
        user = await self.user_repo.get_by_username(username)

        if not user:
            raise AuthenticationError("Unknown username")

        if not verify_password(password, user.hashed_password):
            raise AuthenticationError("Wrong password")

        token = create_access_token({"sub": user.username, "uid": user.id})
        return token

    # --------------------------
    # VALIDATE TOKEN
    # --------------------------

    async def validate_token(self, token: str) -> UserIdentity:
        try:
            payload = decode_access_token(token)
            username = payload.get("sub")
            user_id = payload.get("uid")

            if username is None or user_id is None:
                raise AuthenticationError("Token missing fields")

            return UserIdentity(id=user_id, username=username)

        except Exception:
            raise AuthenticationError("Invalid or expired token")
