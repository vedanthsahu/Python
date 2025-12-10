import httpx
from fastapi import FastAPI

# Global variable for the client
client: httpx.AsyncClient | None = None

def init_http_client(app: FastAPI):
    """
    Setup async HTTP client lifecycle.
    """

    @app.on_event("startup")
    async def startup_event():
        global client
        client = httpx.AsyncClient(timeout=10.0)

    @app.on_event("shutdown")
    async def shutdown_event():
        global client
        if client:
            await client.aclose()

def get_http_client() -> httpx.AsyncClient:
    """
    Dependency to get the global AsyncClient.
    """
    if not client:
        raise RuntimeError("HTTP client not initialized")
    return client
