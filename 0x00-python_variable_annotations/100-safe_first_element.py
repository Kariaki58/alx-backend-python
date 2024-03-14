#!/usr/bin/env python3
"""Duck typing - first elment"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """commented"""
    if lst:
        return lst[0]
    else:
        return None
