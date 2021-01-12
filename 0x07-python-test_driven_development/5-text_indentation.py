#!/usr/bin/python3
"""Define a function text_indentation"""


def text_indentation(text):
    """
    Prints text with 2 lines after each characters.

    Args:
        text: Text to be printed

    Raises:
         TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    letter = 0
    while letter < len(text) and text[letter] == " ":
        letter += 1

    while letter < len(text):
        print(text[letter], end="")
        if text[letter] == "\n" or text[letter] in ".?:":
            if text[letter] in ".?:":
                print("\n")
            letter += 1
            while letter < len(text) and text[letter] == " ":
                letter += 1
            continue
        letter += 1
