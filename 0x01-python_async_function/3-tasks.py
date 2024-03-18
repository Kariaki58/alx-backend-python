#!/usr/bin/env python3
"""import moudles"""

import asyncio
from typing import Task
from asyncio import create_task

from_module = __import__('0-basic_async_syntax')
wait_random = from_module.wait_random

def task_wait_random(maximum_delay: int) -> Task:
    return create_task(wait_random(maximum_delay))
