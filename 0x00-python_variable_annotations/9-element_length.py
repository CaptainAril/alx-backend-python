#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import List, Tuple, Sequence


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """Returns a list of the lenght of each `lst` item."""
    return [(i, len(i)) for i in lst]
