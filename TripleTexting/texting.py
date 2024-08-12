#!/usr/bin/env python3

import sys

def main():
    lst = []
    s = sys.stdin.readline()

    length = len(s) // 3

    lst.append(s[0:length])
    lst.append(s[length:length * 2])
    lst.append(s[length*2:length * 3])

    word1O = lst.count(lst[0])
    word2O = lst.count(lst[1])
    word3O = lst.count(lst[2])

    if word1O > 1:
        print(lst[0])
        return
    if word2O > 1:
        print(lst[1])
        return
    if word3O > 1:
        print(lst[2])
        return
    
if __name__ == "__main__":
    main()
