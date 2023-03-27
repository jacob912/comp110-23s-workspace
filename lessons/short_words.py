"""Short words function quiz 2 practice."""
__author__ = "730463543"


def short_words(words: list[str]) -> list[str]:
    """Returns a list of words that are shorter than 5 characters."""
    idx: int = 0
    new_words: list[str] = list()
    while idx < len(words):
        if len(words[idx]) < 5:
            new_words.append(words[idx])
            idx += 1
        else:
            print(f"{words[idx]} is too long!")
            idx += 1
    return new_words
