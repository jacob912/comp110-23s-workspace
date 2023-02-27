"""EX04 - `list` Utility Functions"""

__author__ = "730463543"

def all(list_nums: list[int], number: int) -> bool:
    list_idx: int = 0
    while list_idx < len(list_nums):
        if list_nums[list_idx] == number:
            list_idx += 1
        else:
            return False  #returns False if it does not make through while loop
    return True  #returns True if it goes through the whole while loop with the numbers in list and number equal

def max(input: list[int]) -> int:
    input_idx1: int = 1  #starting at the second number in the list so my while loop works
    max_val: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    while input_idx1 < len(input):
        if input[input_idx1] > input[input_idx1 - 1]:  #if the number on the list is bigger than the number before it
            max_val = input[input_idx1]
            input_idx1 += 1
        else:
            if input[input_idx1 - 1] > max_val:  #if the number is bigger than the current max value
                max_val = input[input_idx1 - 1]
                input_idx1 += 1
            else:
                max_val = max_val
                input_idx1 += 1
    return max_val  #returns the max value once it goes through the whole while loop (all of the indexes covered)

def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx_list: int = 0
    if len(list1) == len(list2):  #making sure both lists are equal in length
        while idx_list < len(list1):
            if list1[idx_list] == list2[idx_list]:
                idx_list += 1
            else:
                return False  #returns False if it does not make it through the while loop
        return True  #returns True if it goes through the whole while loop with the lists equaling each other
    else:
        return False  #returns False if they aren't equal in length
