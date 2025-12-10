from fastapi import FastAPI, BackgroundTasks
import httpx
import asyncio

app = FastAPI()

# ----------------------------------------------------------------------
# Helper async functions (email & logger)
# ----------------------------------------------------------------------

async def send_email(email: str) -> None:
    # Simulate slow I/O task
    await asyncio.sleep(0.1)
    print("Email sent to:", email)

async def log_action(user: str, status: str) -> None:
    await asyncio.sleep(0.1)
    print(f"Log entry → user={user}, status={status}")


# ----------------------------------------------------------------------
# Endpoint 1 — Demonstrates asyncio.gather (order-preserving concurrency)
# ----------------------------------------------------------------------

@app.get("/basicSync")
async def getURLData():
    """
    Demonstrates asyncio.gather:
    - Runs all coroutines concurrently
    - Returns results in the SAME ORDER they were provided
    - Best when order matters
    """
    async with httpx.AsyncClient() as client:

        # These two HTTP requests run concurrently
        r1, r2 = await asyncio.gather(
            client.get("https://jsonplaceholder.typicode.com/posts"),
            client.get("https://jsonplaceholder.typicode.com/users")
        )

    return {
        "posts_status": r1.status_code,
        "users_status": r2.status_code
    }


# ----------------------------------------------------------------------
# Endpoint 2 — Demonstrates asyncio.as_completed (fastest-first results),
# sequential awaits, and background tasks
# ----------------------------------------------------------------------

@app.get("/multitaskSync")
async def getdata(background: BackgroundTasks) -> str:
    """
    Demonstrates:
    - asyncio.as_completed → process responses in the order they FINISH
    - sequential awaits → slower, non-concurrent
    - BackgroundTasks → run AFTER returning response (not concurrent)
    """
    async with httpx.AsyncClient() as client:

        # --------------------------------------------------------------
        # 1. Using asyncio.as_completed (fastest response first)
        # --------------------------------------------------------------

        coros = [
            client.get("https://jsonplaceholder.typicode.com/posts"),
            client.get("https://jsonplaceholder.typicode.com/users")
        ]

        results = []
        # Process whichever finishes first
        for coro in asyncio.as_completed(coros):
            resp = await coro
            results.append(resp)

        r1, r2 = results  # fastest response → r1

        # --------------------------------------------------------------
        # 2. Sequential awaits (slow, non-concurrent)
        # --------------------------------------------------------------

        r3 = await client.get("https://jsonplaceholder.typicode.com/posts")
        r4 = await client.get("https://jsonplaceholder.typicode.com/posts")

        # --------------------------------------------------------------
        # 3. FastAPI Background Tasks
        # Runs ONLY after returning response to the user.
        # NOT threads, NOT asyncio tasks, just deferred execution.
        # --------------------------------------------------------------

        background.add_task(send_email, "vedanth@gmail.com")
        background.add_task(log_action, user="vedanth", status="success")

        # --------------------------------------------------------------
        # Return combined HTTP status codes
        # --------------------------------------------------------------

        return (
            f"{r1.status_code} | "
            f"{r2.status_code} | "
            f"{r3.status_code} | "
            f"{r4.status_code}"
        )

# ----------------------------------------------------------------------
# Explanation of async usage:
#
# Async = best for I/O-bound tasks (HTTP calls, DB calls, file I/O)
# Threads = also for I/O-bound tasks, especially when blocking libraries
# Processes = for CPU-bound tasks (heavy computation)
#
# GIL allows only ONE thread to execute Python bytecode at a time, but it
# releases during I/O, allowing concurrency in I/O tasks.
# ----------------------------------------------------------------------

async def cpuHeavyTask(var : str) -> None:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, "HeavyTask", 10)
    return result

'''
This is used when we have a CPU heavy task which we have to do
but using the same thread will make all other processes blocked
so to deal with this, we can move this heavy task to another thread in this way we can makesure
That the initial thread is not blocked and can continue other tasks and 
once the result is ready we can use the result.
'''