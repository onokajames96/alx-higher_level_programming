#!/usr/bin/python3
def uppercase(str):
    for num in str:
        if 97 <= ord(num) <= 122:
            num = chr(ord(num) - 32)
            print("{}".format(num), end='')
    print()
