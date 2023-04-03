#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of ints and floats
    and returns the sum of list items.
    """
    return sum(mxd_lst)
