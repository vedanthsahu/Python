from contextlib import asynccontextmanager
from httpx import AsyncClient
import asyncio

# Global shared resources
http_client: AsyncClient | None = None
running_tasks: set[asyncio.Task] = set()


@asynccontextmanager
async def lifespan(app):
    """
    Lifespan context manager for:
    - creating reusable httpx.AsyncClient
    - tracking background tasks
    - graceful shutdown of running tasks
    """

    global http_client
    http_client = AsyncClient(timeout=10.0)

    print("🚀 Application startup: HTTP client initialized")

    try:
        yield

    finally:
        # Cancel running tasks gracefully
        for task in running_tasks:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        # Close the global HTTP client
        if http_client:
            await http_client.aclose()

        print("🛑 Application shutdown: cleaned up resources")
