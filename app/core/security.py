from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from core.config import get_settings


settings = get_settings()

# Password hashing system
pwd_context = CryptContext(
    schemes=[settings.PASSWORD_HASH_SCHEME],
    deprecated="auto"
)


# ------------------------------
# Password Hashing
# ------------------------------

def hash_password(password: str) -> str:
    """
    Hashes plaintext password using bcrypt.
    """
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    """
    Validates a plaintext password against stored hash.
    """
    return pwd_context.verify(plain, hashed)


# ------------------------------
# JWT TOKEN CREATION
# ------------------------------

def create_access_token(data: dict) -> str:
    """
    Generates a signed JWT access token.
    Expiry time injected into payload.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )

    return token


# ------------------------------
# JWT VERIFICATION
# ------------------------------

def decode_access_token(token: str) -> dict:
    """
    Decodes and validates a JWT access token.
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload

    except JWTError:
        raise ValueError("Invalid or expired token")
