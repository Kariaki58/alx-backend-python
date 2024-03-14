#!/usr/bin/env python3
"""import modules"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of inputlist and returns a float"""
    sum = 0.0
    for data in input_list:
        sum += data
    return sum
