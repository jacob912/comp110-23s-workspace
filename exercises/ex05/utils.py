"""EX05 - 'list' Utility Functions."""

__author__ = "730463543"


def only_evens(list_nums: list[int]) -> list[int]:
    """Function that returns only the even numbers from a list given to it."""
    list_idx: int = 0
    return_list: list[int] = list()
    if len(list_nums) > 0:
        while list_idx < len(list_nums):
            if list_nums[list_idx] % 2 == 0:
                return_list.append(list_nums[list_idx])
                list_idx += 1
            else:
                list_idx += 1
        return return_list
    else:
        return return_list
    

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Function that takes in two lists of integers and returns a list that combines the two."""
    list_idx: int = 0
    combined_list: list[int] = list()
    while list_idx < len(list1):
        combined_list.append(list1[list_idx])
        list_idx += 1
    list_idx = 0
    while list_idx < len(list2):
        combined_list.append(list2[list_idx])
        list_idx += 1
    return combined_list


def sub(list_nums: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Generate a list that is a subset of the given list between the two indexes (end idx not inclusive)."""
    current_idx: int = 0
    return_list: list[int] = list()
    if len(list_nums) == 0 or start_idx >= len(list_nums) or end_idx <= 0:
        return return_list
    if start_idx < 0:
        start_idx = 0
    if end_idx >= len(list_nums):
        end_idx = len(list_nums)
    while current_idx < end_idx:
        if current_idx >= start_idx:
            return_list.append(list_nums[current_idx])
            current_idx += 1
        else:
            current_idx += 1
    return return_list