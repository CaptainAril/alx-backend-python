#!/usr/bin/env python3
"""Async Comprehension."""

from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator:
    """Coroutine that loops 10 times
    and yields a random number between 0 and 10."""
    for i in range(10):
        yield random.uniform(0, 10)
