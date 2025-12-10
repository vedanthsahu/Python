from fastapi import APIRouter, Depends
import asyncio
import random

from services.async_task import (
    simulated_work,
    fire_and_forget,
    run_concurrent_gather,
    run_concurrent_as_completed,
    run_with_timeout,
    cancelable_task,
    limited_concurrency,
)
from api.auth import get_current_user

router = APIRouter()


# --------------------------
# GATHER EXAMPLE
# --------------------------

@router.get("/gather")
async def gather_example(user=Depends(get_current_user)):
    tasks = [
        simulated_work("A", 2),
        simulated_work("B", 1),
        simulated_work("C", 3)
    ]
    return await run_concurrent_gather(tasks)


# --------------------------
# AS_COMPLETED EXAMPLE
# --------------------------

@router.get("/as-completed")
async def as_completed_example(user=Depends(get_current_user)):
    tasks = [
        simulated_work("A", 2),
        simulated_work("B", 1),
        simulated_work("C", 3)
    ]
    return await run_concurrent_as_completed(tasks)


# --------------------------
# FIRE-AND-FORGET EXAMPLE
# --------------------------

@router.get("/background")
async def fire_and_forget_example(user=Depends(get_current_user)):
    fire_and_forget(simulated_work("BG", 5))
    return {"status": "background task running"}


# --------------------------
# TIMEOUT EXAMPLE
# --------------------------

@router.get("/timeout")
async def timeout_example(user=Depends(get_current_user)):
    return await run_with_timeout(simulated_work("slow", 3), timeout=1)


# --------------------------
# CANCELLABLE TASK
# --------------------------

@router.get("/cancel")
async def cancel_example(user=Depends(get_current_user)):
    task = asyncio.create_task(cancelable_task("demo", 5))

    await asyncio.sleep(1)
    task.cancel()

    return await task


# --------------------------
# CONTROLLED CONCURRENCY
# --------------------------

@router.get("/semaphore")
async def semaphore_example(user=Depends(get_current_user)):

    def make_factory(i):
        return lambda: simulated_work(f"T{i}", random.uniform(0.5, 2.5))

    factories = [make_factory(i) for i in range(10)]

    return await limited_concurrency(factories, max_concurrent=3)
