#!/usr/bin/python3
"""
Text indentation

Creating date: May 22,2020.

Author: Carlos Murcia.
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of ., ?,:.

    Arguments:
    text: given text.

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    c = [".", "?", ":"]
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in c:
            print()
            print()
            if text[i + 1] == " ":
                i += 1
        i += 1