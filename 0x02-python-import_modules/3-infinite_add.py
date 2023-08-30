#!/usr/bin/python3
if __name__ == "__main__":
    result = 0

    import sys

    for k in range(1,len(sys.argv)):
        result += int(sys.argv[k])
        print("{}".format(result))
