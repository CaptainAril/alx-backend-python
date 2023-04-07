#!/usr/bin/env python3
"""Creating coroutines."""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Takes an integer `max_delay` and returns a async task"""
    task = create_task(wait_random(max_delay))
    return task
