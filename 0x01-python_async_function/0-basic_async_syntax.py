#!/usr/bin/env python3
"""the basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait random function"""
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
