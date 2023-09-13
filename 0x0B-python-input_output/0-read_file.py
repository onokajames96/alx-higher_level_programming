#!/usr/bin/python3
"""A function that reads a Text file."""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
