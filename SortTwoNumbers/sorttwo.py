#!/bin/usr/env python3


def main():
    l = [int(i) for i in input().split()]

    print("{0} {1}".format(min(l), max(l)))

if __name__ == "__main__":
    main()