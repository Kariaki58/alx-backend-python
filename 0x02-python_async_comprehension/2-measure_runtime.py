#!/usr/bin/env python3
"""time and asyncio"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime"""
    start = time.perf_counter()
    coroutine = []
    for _ in range(4):
        coroutine.append(async_comprehension())
    await asyncio.gather(*coroutine)
    end = time.perf_counter()
    return end - start
