#!/usr/bin/python3
"""this module hold text_indentation function definition
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
    ".", "?" and ":"

    Args:
        text (str): the text to perform the operation on
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = "".join([ch + "\n\n" if ch in ".?:" else ch for ch in text])
    print("\n".join([line.strip() for line in result.split("\n")]), end="")
