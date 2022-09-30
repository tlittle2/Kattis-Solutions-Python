#!/usr/bin/env python3
import sys


def main():
    values = sys.stdin.readline().split()
    answer = 1
    for i in values:
        answer*=int(i)
    
    print(answer)





if __name__ == "__main__":
    main()