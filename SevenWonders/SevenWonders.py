#/usr/bin/env python3

import sys

def main():
    string = list(i for i in sys.stdin.readline().strip())
    listofCounts = []
    total =0
    
    gCount= string.count("G")
    listofCounts.append(gCount)
    cCount= string.count("C")
    listofCounts.append(cCount)
    tCount= string.count("T")
    listofCounts.append(tCount)

    total= gCount ** 2 + cCount ** 2+ tCount **2 + (7 * min(listofCounts))
    print(total)

if __name__ == "__main__":
    main()