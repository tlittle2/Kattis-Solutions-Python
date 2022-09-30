#!/bin/usr/env python3

def main():
    n = int(input())

    lst = list()

    for i in range(n):
        lst.append(int(input()))

    print(lst)

    newVal = lst[0]
    newCompare= 1
    for i in range(newCompare, len(lst)):
        print("{} % {} = {}".format(lst[newCompare], newVal, (lst[newCompare] % newVal)))
        if lst[newCompare] % newVal == 0:
            print(lst[newCompare])
            newVal= lst[newCompare + 1]
            newCompare= lst[newCompare + 2]
            print(newVal, newCompare)
            return
        else:
            newCompare+=1








if __name__ == "__main__":
    main()