#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that takes multiplies a number
    with `multiplier`.
    """
    def mul(n):
        return n * multiplier
    return mul
