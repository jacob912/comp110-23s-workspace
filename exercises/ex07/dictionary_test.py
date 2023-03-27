"""EX07 - Tests for Dictionary Functions."""

__author__ = "730463543"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest

def test_letter_dict() -> None:
    """Testing a regular dictionary being inputted that only contains letters."""
    test_dict: dict[str, str] = {'a': 'b', 'b': 'c', 'c': 'd'}
    assert invert(test_dict) == {'b': 'a', 'c': 'b', 'd': 'c'}


def test_word_dict() -> None:
    """Testing a regular dictionary being inputted that only contains words."""
    test_dict: dict[str, str] = {'UNC': 'Tarheels', 'Duke': 'Devils', 'State': 'Wolfpack'}
    assert invert(test_dict) == {'Tarheels': 'UNC', 'Devils': 'Duke', 'Wolfpack': 'State'}


def test_repeating_val_dict() -> None:
    """Testing a dictionary where the inputted dictionary has a repeating value, which would cause a KeyError - Edge Case."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {'Carolina': 'Panthers', 'Pittsburgh': 'Panthers', 'Florida': 'Panthers'}
        invert(test_dict)


def test_all_same() -> None:
    """Testing when the inputted dictionary is all the same strings on indexes and values - Edge case."""
    test_dict: dict[str, str] = {'UNC': 'UNC', 'UNC': 'UNC', 'UNC': 'UNC'}
    assert invert(test_dict) == {'UNC': 'UNC', 'UNC': 'UNC', 'UNC': 'UNC'}


def test_reg_dict() -> None:
    """Testing where the inputted dictionary is regularly formatted."""
    test_dict: dict[str, str] = {'Jacob': 'blue', 'Jon': 'blue', 'Mary': 'green', 'Josh': 'red'}
    assert favorite_color(test_dict) == "blue"


def test_all_one_color() -> None:
    """Testing where the inputted dictionary's people all have the same favorite color."""
    test_dict: dict[str, str] = {'Jacob': 'red', 'Jon': 'red', 'Mary': 'red', 'Josh': 'red'}
    assert favorite_color(test_dict) == "red"


def test_all_different() -> None:
    """Testing where all the responses of favorite color are different - Edge case."""
    test_dict: dict[str, str] = {'Jacob': 'blue', 'Jon': 'red', 'Mary': 'green', 'Josh': 'yellow'}
    assert favorite_color(test_dict) == "blue"


def test_reg_list() -> None:
    """Testing where the inputted list is a regular str list."""
    test_list: list[str] = ["UNC", "Duke", "UNC", "App", "UNCC", "UNC"]
    assert count(test_list) == {"UNC": 3, "Duke": 1, "App": 1, "UNCC": 1}


def test_all_different() -> None:
    """Testing when the inputted list is all different strings."""
    test_list: list[str] = ["UNC", "Duke", "State", "App", "UNCC"]
    assert count(test_list) == {"UNC": 1, "Duke": 1, "State": 1, "App": 1, "UNCC": 1}


def test_all_same() -> None:
    """Testing when the inputted list is all the same string - Edge case."""
    test_list: list[str] = ["UNC", "UNC", "UNC", "UNC", "UNC", "UNC", "UNC"]
    assert count(test_list) == {"UNC": 7}