#!/usr/bin/python3
import sys


if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(i))
    for n in range(i):
        print("{}: {}".format(n+1, sys.argv[n+1]))
