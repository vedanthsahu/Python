import asyncio
import random
from typing import List, Callable, Awaitable, Any


# --------------------------
# BASIC SIMULATED WORK
# --------------------------

async def simulated_work(name: str, duration: float):
    await asyncio.sleep(duration)
    return f"Task {name} completed in {duration}s"


# --------------------------
# FIRE-AND-FORGET
# --------------------------

def fire_and_forget(coro: Awaitable):
    """
    Launch a background async task that should run independently.
    """
    task = asyncio.create_task(coro)

    # Prevent "task destroyed but pending" if unhandled error
    task.add_done_callback(lambda t: t.exception())

    return task


# --------------------------
# GATHER (ORDERED RESULTS)
# --------------------------

async def run_concurrent_gather(coros: List[Awaitable]):
    """
    Runs tasks concurrently and returns results in the
    SAME order as provided.
    """
    return await asyncio.gather(*coros)


# --------------------------
# AS_COMPLETED (FASTEST-FIRST)
# --------------------------

async def run_concurrent_as_completed(coros: List[Awaitable]):
    """
    Iterates results in the order they finish.
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
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
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
# CONTROLLED CONCURRENCY
# SEMAPHORE PATTERN
# --------------------------

async def limited_concurrency(coros: List[Callable[[], Awaitable]], max_concurrent: int):
    semaphore = asyncio.Semaphore(max_concurrent)
    results = []

    async def run_one(coro_factory: Callable[[], Awaitable]):
        async with semaphore:
            return await coro_factory()

    tasks = [asyncio.create_task(run_one(factory)) for factory in coros]

    for t in asyncio.as_completed(tasks):
        results.append(await t)

    return results
