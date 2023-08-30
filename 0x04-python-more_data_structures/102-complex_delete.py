#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()

    while value in new_dict.values():

        for key, val in new_dict.items():
            if val == value:

                del new_dict[key]
                break

    return new_dict
