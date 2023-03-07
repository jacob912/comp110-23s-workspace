"""Using for loop to make sum function"""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for float in xs:
        sum_total += float
    return sum_total