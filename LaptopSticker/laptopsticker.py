#!usr/bin/env python3


def main():
    wc, hc, ws, hs = map(int, input().split())

    if wc - ws < 2 or hc - hs < 2:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()