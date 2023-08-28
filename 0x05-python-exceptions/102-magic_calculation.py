#!/usr/bin/python3
def magic_calculation(a, b):

    output = 0

    for new_list in range(1, 3):
        try:
            if new_list > a:
                raise Exception('Too far')
            output = output + (a ** b) / new_list
        except:
            output = b + a
            break
        return output
