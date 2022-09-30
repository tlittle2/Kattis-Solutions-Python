#!/usr/bin/env python3



def fib(n):
    s= ""
    if n == 0:
        s+= "0"
    elif n == 1:
        s+= "1"
    else:
        s+= fib(n-1) + fib(n-2)

    return s

def main():
    num = (int(input().strip()))
    seq = input().strip()

    newNum = fib(num)
    print(newNum)
    print(newNum.count(seq))

if __name__ == "__main__":
    main()