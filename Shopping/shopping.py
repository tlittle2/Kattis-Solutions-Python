#!/bin/usr/env python3

def main():
    d = {}
    lsts, items = map(int, input().split())

    for i in range(lsts):
        item = input().split()[:items]
        #print(item)
        for j in item:
            
            if j in d.keys():
                d[j]+=1
            if j not in d.keys():
                d[j] = 1
    
    
    #print(d)
    count=0
    for k, v in d.items():
        if v == lsts:
            count+=1
    print(count)


    aList = list()
    for k, v in d.items():
        if v == lsts:
            aList.append(k)

    aList.sort()
    for i in aList:
        print(i)
    

if __name__ == "__main__":
    main()