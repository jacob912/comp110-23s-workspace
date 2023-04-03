"""EX07 - Dictionary Functions."""

__author__ = "730463543"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """A function that inverts the dictionary inputted into it."""
    return_dict: dict[str, str] = dict()
    for elem in input_dict:
        if input_dict[elem] in return_dict:
            raise KeyError
        else: 
            return_dict[input_dict[elem]] = elem
    return return_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """A function that takes peoples' favorite colors and says which color is stated the most."""
    count_dict: dict[str, int] = dict()
    high_score: int = 0
    fav_color: str = ""
    for elem in input_dict:
        if input_dict[elem] in count_dict:
            count_dict[input_dict[elem]] += 1
        else:
            count_dict[input_dict[elem]] = 1
    for elem in count_dict:
        if count_dict[elem] > high_score:
            high_score = count_dict[elem]
            fav_color = elem
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """A function that takes a list and produces a dictionary with the count of how many times each thing appears in the list."""
    return_dict: dict[str, int] = dict()
    for elem in input_list:
        if elem in return_dict:
            return_dict[elem] += 1
        else:
            return_dict[elem] = 1
    return return_dict