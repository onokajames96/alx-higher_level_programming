#!/usr/bin/python3
def remove_char_at(str, n):
    if not(0 <= n < len(str)):
        return(str)
    string = ""
    for j in range(len(str)):
        if j != n:
            string += str[j]

    return (string)
