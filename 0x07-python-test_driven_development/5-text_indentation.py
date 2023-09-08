#!/usr/bin/python3

"""module text_indentation"""

def text_indentation(text):
    """ defination"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char

        if char in (".", "?", ":"):
            print(buffer.strip())
            buffer = ""

    if buffer:
        print(buffer.strip())
