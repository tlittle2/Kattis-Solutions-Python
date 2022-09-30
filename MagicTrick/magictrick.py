#!/usr/bin/env python3


def main():
    n = input()
    b = False

    for i in n:
        if n.count(i) > 1:
            b = True
            break
    if b:
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    main()