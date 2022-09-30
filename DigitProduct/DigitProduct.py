#/usr/bin/env python3
import sys

def multiply(num):
    answer = 1
    num = [i for i in num if i != 0]

    for i in num:
        answer *= i

    answer = str(answer)
    ansList = []

    for i in answer:
        i = int(i)
        ansList.append(i)

    if len(ansList) == 1:
        print(ansList.pop())
        return
    else:
        multiply(ansList)

def main():
    number= list(map(int, sys.stdin.readline().strip()))

    multiply(number)

if __name__ == "__main__":
    main()