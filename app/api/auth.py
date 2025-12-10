from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from schemas.auth import LoginRequest, TokenResponse, UserIdentity
from services.auth_service import AuthService
from domain.exceptions import AuthenticationError


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# --------------------------
# LOGIN ENDPOINT
# --------------------------

@router.post("/login", response_model=TokenResponse)
async def login(
    body: LoginRequest,
    auth_service: AuthService = Depends()
):
    try:
        token = await auth_service.login(body.username, body.password)
        return TokenResponse(access_token=token)

    except AuthenticationError as ex:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(ex)
        )


# --------------------------
# AUTHENTICATED USER DEPENDENCY
# --------------------------

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends()
) -> UserIdentity:
    try:
        return await auth_service.validate_token(token)

    except AuthenticationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication"
        )
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from services.auth_service import AuthService

router = APIRouter(prefix="/auth")

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

auth_service = AuthService()  # Make sure this uses your UserRepository

@router.post("/register")
async def register_user(data: RegisterRequest):
    try:
        user = await auth_service.user_repo.create_user(data.email, data.password)
        return {"email": user.email, "message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

