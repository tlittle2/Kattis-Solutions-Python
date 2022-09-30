#!/usr/bin/env python3

def main():
    n = int(input())

    print(int(n * (n - 1) * (n - 2) * (n - 3) / (1 * 2 * 3 * 4)))


if __name__ == "__main__":
    main()