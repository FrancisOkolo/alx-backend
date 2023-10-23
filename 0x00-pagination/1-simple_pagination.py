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
        res = index_range(page, page_size)
        return res