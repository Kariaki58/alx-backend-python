#!/usr/bin/env python3
"""import function"""
import asyncio
from typing import List, Task
from asyncio import create_task

from_module = __import__('1-concurrent_coroutines')
wait_n = from_module.wait_n
task_wait_random = __import__('3-tasks').task_wait_random

def task_wait_n(n: int, max_delay: int) -> Task[List[float]]:
    """task wait n"""
    async def execute_task_wait_random():
        """execute task wait randome"""
        return await task_wait_random(max_delay)

    async def execute_wait_n():
        """execute wait n"""
        return await wait_n(n, max_delay)

    return create_task(execute_task_wait_random() if n == 1 else execute_wait_n())

