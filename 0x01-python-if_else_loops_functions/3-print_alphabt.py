#!/usr/bin/python3
for num in range(97, 123):
    if chr(num) != 'q' and chr(num) != 'e':
        print("{:s}".format(chr(num)), end='')
