#!/usr/bin/env python3
"""import modules"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    tup = (k, v ** 2)
    return tup
