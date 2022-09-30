#!/usr/bin/env python3



def fibWord(n):
    Sn_1 = "0"
    Sn = "01"
    tmp = ""
    for i in range(2, n + 1):
        tmp = Sn
        Sn += Sn_1
        Sn_1 = tmp
    return Sn


def main():
    num = (int(input().strip()))
    seq = input().strip()

    newNum = fibWord(num)
    print(newNum)
    print(newNum.count(seq))

if __name__ == "__main__":
    main()