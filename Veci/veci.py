#!/usr/bin/env python3

import itertools

def main():
    n = str(input())

    perms = list(itertools.permutations(n))

    perms = ([''.join(p) for p in perms])


    
    for i in range(len(perms)):
        perms[i] = int(perms[i])

    

    n = int(n)
    mstrList = []

    for i in perms:
        if i not in mstrList:
            mstrList.append(i)

    mstrList.sort()


    for i in range(len(mstrList)): 
        if mstrList[i] == n:
            if i + 1 != len(mstrList):
                print(mstrList[i+1])
            else:
                print(0)

    

if __name__ == "__main__":
    main()