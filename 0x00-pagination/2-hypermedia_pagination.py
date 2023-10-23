#!/usr/bin/env python3
"""implement the helper function
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''simple helper function'''

    last_obj = page * page_size
    first_obj = last_obj - page_size
    return first_obj, last_obj


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ implement the helper function
        """
        assert isinstance(page, int), "page and/or page_size are not ints"
        assert isinstance(page_size, int), "page and/or page_size are not ints"
        assert page > 0, "raised with negative values"
        assert page_size > 0, "raised with negative values"

        wrapper = self.dataset()
        if (page_size - page) > len(wrapper):
            return []
        first, last = index_range(page, page_size)
        return wrapper[first:last]

    def get_hyper(self, page: int, page_size: int) -> dict:
        """Hypermedia pagination"""
        data = self.get_page(page, page_size)
        size_all_pages = math.ceil(len(self.get_dataset()) / page_size)
        next_page = page + 1 if page + 1 < size_all_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": size_all_pages,
        }

        return hyper_data
