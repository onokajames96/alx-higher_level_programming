#!/usr/bin/python3
"""A text file insertion function defined"""


def append_after(filename="", search_string="", new_string=""):
    """ 
    The function that inserts a line of text to a file,
    after each line containing a specific str.
    """

    content = ""

    with open(filename, "r") as r:
        for line in r:
            content += line
            if search_string in line:
                content += new_string

    with open(filename, "w") as w:
        w.write(content)

