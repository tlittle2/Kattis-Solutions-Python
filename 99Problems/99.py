#!/bin/usr/env python3

# the key is to interpret the numbers as strings first so that we can properly manipulate them
    # after manipulation, then interpret them as integers to do the comparisons

def main():
    n = input()

    if int(n) < 100:
        print(99)
        return

    #get all the digits up until the last 2
    firstN = n[0:len(n)-2]

    #print(firstN)

    #subtract 1 from the value up until the last 2 digits
    lowerCompare = str(int(firstN) - 1)
    
    #append the lower part, and add a 99 to get the lower number
    lowerNum = str(lowerCompare + str(99))

    #the higher number should always be the the same up to the last 2 digits, where we will append 99 to the end
    higherNum = str(firstN + str(99))
    #print(lowerNum, higherNum)

    #find the 2 differences
    lDiff = int(n)-int(lowerNum)
    hDiff= int(higherNum) - int(n)

    # if the difference are the same, pick the higher number
    if lDiff == hDiff:
        print(higherNum)
        return
    
    #of the 2 differences, which one is the lower (this will be equal the closest value)
    if lDiff < hDiff:
        print(int(lowerNum))
    else:
        print((higherNum))



if __name__ == "__main__":
    main()