 explain sync vs async clearly in my own words. 

 what the event loop, coroutine, and task are.

 why await is required and what happens if I forget it.

why blocking calls like time.sleep() are bad in async code.

 use asyncio.gather to run I/O tasks concurrently. 

 write FastAPI async endpoints that call external APIs.

 implement a background task in FastAPI for non-critical work.

 create and activate a virtual environment and manage dependencies.

how Poetry and pipx fit into a backend workflow.

 add clear type hints to all functions and classes in a module.

 how to use List, Dict, Optional, Union, Callable, and TypeAlias.

 define Pydantic v2 models and validators and explain model_validate vs model_dump.

 wire Pydantic models as request/response schemas in FastAPI with response_model.

 design domain-specific exceptions and a base AppError.

 implement a centralized FastAPI exception handler that returns consistent JSON errors.

 how to configure Python logging, and when to use INFO/DEBUG/WARNING/ERROR.

 explain what dependency injection is and why it helps testing.

 use FastAPI Depends + Annotated to inject repositories/services.

 design and implement a small CRUD API with JWT auth, pagination, logging, and error handling.




Async fundamentals (event loop, await, gather)

Async in FastAPI (endpoints, httpx, background tasks)

Type hints & typing module usage

Pydantic v2 models & validators

Exceptions (design + usage)

Logging (configuration + good practices)

Dependency injection & architecture (repo/service layers)

Packaging & environment management (venv, Poetry)