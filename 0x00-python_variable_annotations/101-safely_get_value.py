#!/bin/usr/env python3
"""more involed type annotations"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """safe get value"""
    if key in dct:
        return dct[key]
    else:
        return default
