#!/usr/bin/env python3
"""the basics of async"""
import random


async def wait_random(max_delay :int = 10) -> float:
    """wait random function"""
    return random.uniform(0, max_delay)