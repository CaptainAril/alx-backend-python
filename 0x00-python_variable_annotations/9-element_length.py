#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of the lenght of each `lst` item."""
    return [(i, len(i)) for i in lst]
