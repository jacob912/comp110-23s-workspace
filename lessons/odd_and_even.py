"""Writing a odd_and_even function."""

def odd_and_even(ints : list[int]) -> list[int]:
    return_list: list[int] = list()
    idx: int = 0
    while idx < len(ints):
        if idx % 2 == 0 and ints[idx] % 2 != 0:
            return_list.append(ints[idx])
            idx += 1
        else:
            idx += 1
    return return_list