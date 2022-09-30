#!/usr/bin/env python3


def main():
    d = dict()
    d2 = list()
    n = int(input())

    for i in range(n):
        name, num, birth = input().split()
        num = int(num)

        

        print("BIRTH: {}".format(birth))
        if birth not in d:
            d[birth] = name
            d2[birth] = num


        
        print(d)
        print(d2)


if __name__ == "__main__":
    main()