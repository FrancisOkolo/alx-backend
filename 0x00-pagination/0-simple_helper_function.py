#!/usr/bin/env python3
''' A helper function to that returns a tuple of
pagination limits'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''simple helper function'''
    
    last_obj = page * page_size
    first_obj = last_obj - page_size
    return first_obj, last_obj