"""EX05 - 'list' Utility Functions tests."""

__author__ = "730463543"

from exercises.ex05.utils import only_evens

def test_all_evens() -> None:
    test_list: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(test_list) == [2, 4, 6, 8, 10]

def test_random_numbers() -> None:
    test_list: list[int] = [3, 2, 5, 9, 10, 6, 8]
    assert only_evens(test_list) == [2, 10, 6, 8]

def test_no_numbers() -> None:
    test_list: list[int] = []
    assert only_evens(test_list) == []

from exercises.ex05.utils import concat

def test_reg_lists() -> None:
    test_list1: list[int] = [1, 3, 4, 8]
    test_list2: list[int] = [9, 8, 7]
    assert concat(test_list1, test_list2) == [1, 3, 4, 8, 9, 8, 7]

def test_neg_lists() -> None:
    test_list1: list[int] = [-1, -3, -4, -8]
    test_list2: list[int] = [-9, -8, -7]
    assert concat(test_list1, test_list2) == [-1, -3, -4, -8, -9, -8, -7]

def test_empty_lists() -> None:
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []

from exercises.ex05.utils import sub

def test_reg() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5]
    test_start_idx: int = 1
    test_end_idx: int = 3
    assert sub(test_list, test_start_idx, test_end_idx) == [2, 3]

def test_negatives() -> None:
    test_list: list[int] = [-1, -2, -3, -4, -5]
    test_start_idx: int = 1
    test_end_idx: int = 3
    assert sub(test_list, test_start_idx, test_end_idx) == [-2, -3]

def test_end_idx_bigger() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5]
    test_start_idx: int = 1
    test_end_idx: int = 10
    assert sub(test_list, test_start_idx, test_end_idx) == [2, 3, 4, 5]


