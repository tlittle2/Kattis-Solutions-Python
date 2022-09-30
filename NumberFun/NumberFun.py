#/usr/bin/env python3

import sys

def main():
    testCases= int(sys.stdin.readline())

    for i in range(testCases):
        a, b, c= map(int, sys.stdin.readline().split())

        if a+ b ==c:
            print("Possible")
        elif a-b ==c:
            print("Possible")
        elif b-a==c:
            print("Possible")
        elif a * b== c:
            print("Possible")
        elif a / b==c:
            print("Possible")
        elif b/a==c:
            print("Possible")

        else:
            print("Impossible")

if __name__ == '__main__':
    main()