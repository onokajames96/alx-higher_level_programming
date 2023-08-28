#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for new_list in range(1, 3):
        try:
            if new_list > a:
                raise Exception('Too far')
            else:
            result = result + (a ** b) / new_list
        except Exception as e:
            result = b + a
            break
        return result
