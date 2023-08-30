#!/usr/bin/python3
def weight_average(my_list=[]):
    """ calculating the weighted average of integers in a list of tuples.
    """
    if not isinstance(my_list, list) or len(my_list) == "":
        return 0

    average = 0
    size = 0

    for tuple in my_list:
        average += (tuple[0] * tuple[1])
        size += tuple[1]
    return average / size
