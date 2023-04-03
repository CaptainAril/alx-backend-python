#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first item of `lst` if it is an iterable."""
    if lst:
        return lst[0]
    else:
        return None
