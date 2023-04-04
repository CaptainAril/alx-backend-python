#!/usr/bin/env python3
"""Async Comprehension."""

import random
import asyncio
from typing import Iterator


async def async_generator() -> Iterator[int]:
    """Coroutine that loops 10 times
    and yields a random number between 0 and 10."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
