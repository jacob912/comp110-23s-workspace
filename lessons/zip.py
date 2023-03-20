"""CQ04 - Zip."""

def zip(strs: list[str], ints: list[int]) -> dict[str, int]:
    return_dict: dict[str, int] = {}
    idx: int = 0
    if len(strs) != len(ints):
        return return_dict
    while idx < len(strs):
        return_dict[strs[idx]] = ints[idx]
        idx += 1
    return return_dict