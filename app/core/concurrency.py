import asyncio
from typing import List, Callable, Awaitable, Any

# --------------------------
# FIRE-AND-FORGET
# --------------------------
def fire_and_forget(coro: Awaitable):
    """
    Launch a background async task that runs independently.
    """
    task = asyncio.create_task(coro)
    # Ensure unhandled exceptions are logged
    task.add_done_callback(lambda t: t.exception())
    return task


# --------------------------
# GATHER (ORDERED RESULTS)
# --------------------------
async def run_concurrent_gather(coros: List[Awaitable]):
    """
    Run tasks concurrently and return results in the same order as provided.
    """
    return await asyncio.gather(*coros)


# --------------------------
# AS_COMPLETED (FASTEST-FIRST)
# --------------------------
async def run_concurrent_as_completed(coros: List[Awaitable]):
    """
    Iterate results as tasks finish (fastest first).
    """
    results = []
    for task in asyncio.as_completed(coros):
        result = await task
        results.append(result)
    return results


# --------------------------
# TIMEOUT HANDLING
# --------------------------
async def run_with_timeout(coro: Awaitable, timeout: float):
    """
    Run a coroutine with a timeout.
    """
    try:
        return await asyncio.wait_for(coro, timeout)
    except asyncio.TimeoutError:
        return f"Task timed out after {timeout}s"


# --------------------------
# CANCELLATION HANDLING
# --------------------------
async def cancelable_task(name: str, duration: float):
    try:
        await asyncio.sleep(duration)
        return f"{name} finished"
    except asyncio.CancelledError:
        return f"{name} was cancelled"


# --------------------------
# CONTROLLED CONCURRENCY (SEMAPHORE)
# --------------------------
async def limited_concurrency(coros: List[Callable[[], Awaitable]], max_concurrent: int):
    """
    Run multiple coroutines with limited concurrency using a semaphore.
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    results = []

    async def run_one(coro_factory: Callable[[], Awaitable]):
        async with semaphore:
            return await coro_factory()

    tasks = [asyncio.create_task(run_one(factory)) for factory in coros]

    for t in asyncio.as_completed(tasks):
        results.append(await t)

    return results
