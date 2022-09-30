#/usr/bin/env python3

import sys


def factorial(x):
    
    if x== 1:
        return 1
    else:
        output = x * factorial(x-1)
        return output

        

testCase= int(sys.stdin.readline())
answer= 0

for i in range(testCase):
    testInput= int(sys.stdin.readline())
    answer= factorial(testInput) % 10
    print(answer) 