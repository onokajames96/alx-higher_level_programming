#!/usr/bin/python3
for num in range(10):
    for k in range(num +1, 10):
        if num != 8 or k != 9:
            print("{:02}, ".format(num * 10 + k), end='')
print("{:02}".format(89))
