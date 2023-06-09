#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of `k` and the square of `v`."""
    return k, v ** 2
