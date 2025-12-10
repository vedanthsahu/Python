import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from core.logging_config import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # Assign correlation ID
        correlation_id = str(uuid.uuid4())
        request.state.correlation_id = correlation_id

        start = time.time()

        logger.info({
            "msg": "Incoming request",
            "method": request.method,
            "url": str(request.url),
            "client": request.client.host,
            "correlation_id": correlation_id
        })

        # Process request
        response = await call_next(request)

        duration = round((time.time() - start) * 1000, 2)

        logger.info({
            "msg": "Response sent",
            "status": response.status_code,
            "duration_ms": duration,
            "correlation_id": correlation_id
        })

        # Add correlation ID header
        response.headers["X-Correlation-ID"] = correlation_id

        return response
