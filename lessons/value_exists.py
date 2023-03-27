"""Value exists function for quiz 2 practice."""

def value_exists(dict: dict[str,int], num: int) -> bool:
    exists: bool = False
    for elem in dict:
        if dict[elem] == num:
            exists = True
    return exists

