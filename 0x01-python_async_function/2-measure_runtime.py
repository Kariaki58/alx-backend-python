#!/usr/bin/env python3
"""measure the run time"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n, max_delay):
    timer = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - timer
    return total_time / n
