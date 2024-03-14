#!/usr/bin/env python3
"""complex types - fucntions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """documentation 1"""
    def multiply(x: float) -> float:
        """multiply function"""
        return multiplier * x
    return multiply
