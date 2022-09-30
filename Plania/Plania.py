#/usr/bin/env python3

import sys

def main():
    numOfIterations= int(sys.stdin.readline())
    value= 2**numOfIterations+1


    print(value ** 2)

if __name__ == "__main__":
    main()