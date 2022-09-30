#!/usr/bin/env python3

def main():
    n = input()
    for i in range(len(n)-1,-1, -1):
        print(n[i], end="")

    print()



if __name__ == "__main__":
    main()