#!/usr/bin/env python3

""" 9. Let's duck type an iterable object
    Write a type-annotated function element_length with the following
    arguments:
    lst: Iterable[Sequence]
    Returns: List[Tuple[Sequence, int]]
    """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples with sequence and int """
    return [(i, len(i)) for i in lst]
