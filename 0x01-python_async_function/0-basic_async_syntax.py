#!/usr/bin/env python3
"""Creating coroutines."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Takes an interger argument, waits for a random delay
    between 0 and `max_delay` and returns it."""
    wt = random.uniform(0, max_delay)
    await asyncio.sleep(wt)
    return wt
