#!/usr/bin/env python3


import sys

def runE(w):
    current = w[0]
    count = 0
    for c in w:
        if c == current:
            count+=1
        else:
            print("{0}{1}".format(current, count), sep = "", end = "")
            current = c
            count = 1
    print("{0}{1}".format(current, count), sep = "", end = "")



def runD(w):
    for i in range(1, len(w), 2): 
        print(str(w[i-1]) * int(w[i]), sep = "", end = "")
    print()


def main():
    mode, word = sys.stdin.readline().split()

    if mode == "E":
        runE(word)
    else:
        runD(word)




if __name__ == "__main__":
    main()