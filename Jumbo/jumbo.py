#!/usr/bin/env python3


def main():
    n = int(input())
    total = int(input())

    for i in range(n-1):
        v = int(input())
        total+=v - 1

    print(total)




if __name__ == "__main__":
    main()