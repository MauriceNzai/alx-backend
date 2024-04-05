#!/usr/bin/env python3
"""
Pagination helper function that determines the index range, page and page size
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range for pagination given a page and page size.
    return a tuple of size two containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves  the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        # get the data from the csv
        data = self.dataset()
        try:
            # get start and end pages
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves info about a page
        returns this info in a dictionary format
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimating the next page
        if (page < total_pages):
            next_page = page+1
        else:
            next_page = None

        # estimating the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        page_info = {
                'page_size': len(page_data),
                'page': page,
                'data': page_data,
                'next-page': next_page,
                'prev_page': prev_page,  # - 1 if start > 0 else None,
                'total_pages': total_pages
                }
        return page_info
