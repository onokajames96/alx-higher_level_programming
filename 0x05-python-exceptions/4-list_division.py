#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    j = 0

    output_list = []

    while j <list_length:
        try:
            output = my_list_1[j] / my_list_2[j]
        except ZeroDivisionError:
            print("division by 0")
            output = 0
        except TypeError:
            print("wrong type")
            output = 0
        except IndexError:
            print("out of range")
            output = 0
        finally:
            j += 1
            output_list.append(output)

    return output_list
