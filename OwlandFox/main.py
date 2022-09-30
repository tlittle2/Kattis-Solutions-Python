#!/usr/bin/env python3


#delete all leading 0s

import sys

def convertToInt(lst):
    vals = [str(i) for i in lst]

    s = "".join(vals)
    return int(s)

def main():
    for num in sys.stdin:
        num = num.strip()

        if len(num) == 1:
            continue
        else:
            originalSum = 0
            lst = [int(i) for i in num] 
            

            for i in lst:
                originalSum+=i

            #print(lst)
            #print(originalSum)

            for i in range(len(lst)-1, -1, -1):
                if lst[i] - 1 == -1:
                    continue
                else:
                    lst[i] =lst[i] - 1
                    tempSum=0
                    for i in lst:
                        tempSum+=i 
                    if originalSum - 1 == tempSum:
                        print(convertToInt(lst))
                        break
    



if __name__ == "__main__":
    main()