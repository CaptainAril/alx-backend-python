#!/usr/bin/env python3
"""Async Comprehension."""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the total runtime to execute `async_comprehension` four times
    in parallel using `asyncio.gather`."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.time()
    return end - start
