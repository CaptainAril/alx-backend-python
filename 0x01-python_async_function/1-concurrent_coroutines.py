#!/usr/bin/env python3
"""Creating coroutines."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    result = []
    for i in range(n):
        task = await wait_random(max_delay)
        result.append(task)

    temp = 0
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i] < result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result
