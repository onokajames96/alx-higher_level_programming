#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_num = 0

    try:
        for j in range(x):
            if isinstance(my_list[j], int):
                print("{:d}".format(my_list[j]), end="")
                int_num += 1
    except(ValueError):
        pass
    print()
    return int_num

