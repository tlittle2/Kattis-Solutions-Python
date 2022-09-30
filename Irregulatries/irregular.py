#!/usr/bin/env python3

import math


def main():
    numerator = []
    denominator = []
    n = int(input())

    numerator = [int(i) for i in input().split()]

    denominator = [int(i) for i in input().split()]
    
    a = 1
    for i in range(n):
        if numerator[i] <= denominator[i] or denominator[i] == -1:
             continue
        if numerator[i] > denominator[i]:
            #find the closest divisor
            divisor = math.floor(int(numerator[i] / denominator[i]))
            mod = numerator[i] % denominator[i]
            a += divisor + mod - 1
    print(a)




if __name__ == "__main__":
    main()