#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []

    for index in my_list:
        if index == search:
            new.append(replace)
        else:
            new.append(index)
    return new
