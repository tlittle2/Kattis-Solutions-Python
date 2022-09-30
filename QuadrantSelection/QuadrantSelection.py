#/usr/bin/env python3

import sys

def main():
    x= int(sys.stdin.readline())
    y= int(sys.stdin.readline())

    if(x > 0 and y >0):
        print("1")
    elif(x > 0 and y < 0):
        print("4")
    elif(x < 0 and y > 0):
        print("2")
    elif(x < 0 and y < 0):
        print("3")

if __name__ == "__main__":
    main()