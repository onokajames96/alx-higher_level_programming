#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir(hidden_4)
    for k in dir(hidden_4):
        if k[0:2] != "__":
            print(k)
