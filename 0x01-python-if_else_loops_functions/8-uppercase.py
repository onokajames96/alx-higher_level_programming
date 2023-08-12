#!/usr/bin/python3
def uppercase(str):
    for num in str:
        if 'a' <= num <= 'z':
            print(chr(ord(num) - ord('a') + ord('A')), end='')
        else:
            print("{}".format(num), end="")
    print()


