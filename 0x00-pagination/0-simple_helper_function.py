#!/usr/bin/env python3
"""
Pagination helper function that determines the index range, page and page size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range for pagination given a page and page size.
    return a tuple of size two containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
