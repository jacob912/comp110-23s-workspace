"""EX08 - Data Wrangling."""

__author__ = "730463543"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table under a certain header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats our data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(data: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Producing a column-based table with only the first N rows of data for each column."""
    ret_dict: dict[str, list[str]] = {}
    for col in data:
        if num_rows > len(data[col]):
            num_rows = len(data[col])
        head_list: list[str] = list()
        for idx in range(0, num_rows):
            head_list.append(data[col][idx])
        ret_dict[col] = head_list
    return ret_dict
        

def select(data: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selecting a subset of columns."""
    ret_dict: dict[str, list[str]] = dict()
    for elem in names:
        ret_dict[elem] = data[elem]
    return ret_dict


def concat(data1: dict[str, list[str]], data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining two datasets into one."""
    ret_dict: dict[str, list[str]] = dict()
    for col in data1:
        ret_dict[col] = data1[col]
    for col in data2:
        if col in ret_dict:
            ret_dict[col] += data2[col]
        else:
            ret_dict[col] = data2[col]
    return ret_dict


def count(giv_list: list[str]) -> dict[str, int]:
    """Counting how many of each value is in a list."""
    ret_dict: dict[str, int] = dict()
    for elem in giv_list:
        if elem in ret_dict:
            ret_dict[elem] += 1
        else:
            ret_dict[elem] = 1
    return ret_dict