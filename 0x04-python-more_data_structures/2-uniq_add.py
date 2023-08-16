#!/usr/bin/python3
def uniq_add(my_list=[]):
    output_set = set()
    sum = 0
    for i in my_list:
        if i not in output_set:
            sum += i
            output_set.add(i)

    return sum
