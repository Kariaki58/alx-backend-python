#!/usr/bin/env python3
"""import moudles"""
from asyncio import create_task, Task

from_module = __import__('0-basic_async_syntax')
wait_random = from_module.wait_random

def task_wait_random(maximum_delay: int) -> Task:
    """task wait random"""
    return create_task(wait_random(maximum_delay))
