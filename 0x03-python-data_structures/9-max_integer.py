#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != 0:
        return None

    max_value = my_list[0]
    for item in my_list:
        if item > max_value:
            max_value = item
    return max_value

