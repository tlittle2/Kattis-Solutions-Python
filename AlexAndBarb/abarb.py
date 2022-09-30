#!/bin/usr/env python3


def main():
    k, m, n = map(int, input().split())
    
    #starting poitn is m
    #we are always starting with Alex

    print(k % (m+n))
    #adding the start point and the end point and modding by the number of cards we have
    #from here, we can check to who has more moves left using the mod
        #if our modded answer is greater than our starting value, that means that Alex is going to win
        #if our modded answer is elss than our starting alue, that means Barb is going to win
    if k % (m+n) < m:
        print("Barb")
    else:
        print("Alex")





if __name__ == "__main__":
    main()