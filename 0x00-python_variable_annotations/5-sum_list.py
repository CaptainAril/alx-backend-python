#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns the sum of list items.
    """
    return sum(input_list)
