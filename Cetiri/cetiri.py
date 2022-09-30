#!/usr/bin/env python3


def main():
    lst = list(map(int, input().split()))
    lst = sorted(lst, reverse= True)

    const1 = abs(lst[0] - lst[1])
    const2 = abs(lst[1] - lst[2])

    #if const are the same, that means we need to find the number that starts the list
    if const1 == const2:
        print(lst[0] + lst[0] - lst[1])
    elif const1 > const2:
        print(lst[1] + lst[1] - lst[2])

    else:
        print(lst[2] + lst[0] - lst[1])



if __name__ == "__main__":
    main()