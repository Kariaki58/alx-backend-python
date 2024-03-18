#!/usr/bin/python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay_data = random.uniform(0, max_delay)
    await asyncio.sleep(delay_data)
    return delay_data
