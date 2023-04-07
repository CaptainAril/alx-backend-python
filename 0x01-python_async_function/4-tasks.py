#!/usr/bin/env python3
"""Creating coroutines."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns `wait_random` `n` times
    and returns a list of delay periods.
    """

    result = []
    for i in range(n):
        task = await task_wait_random(max_delay)
        result.append(task)

    temp = 0
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i] < result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result
