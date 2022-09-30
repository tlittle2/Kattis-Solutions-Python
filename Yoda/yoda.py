#!/usr/bin/env python3


def findSmallerList(lst1, lst2):
    if len(lst1) < len(lst2):
        return lst1
    else:
        return lst2

def findBiggerList(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1
    else:
        return lst2

def add0s(lst, max):
    while True:
        lst.insert(0,'0')
        if len(lst) == max:
            break

    return lst


def driver(lst1, lst2):
    mstr1 = ""
    mstr2 = ""

    b = True
    for i in range(len(lst1)):
        #print("{} {}".format(lst1[i], lst2[i]))
        if int(lst1[i]) > int(lst2[i]):
            b = False
            mstr1+=lst1[i]
        elif int(lst2[i]) > int(lst1[i]):
            b= False
            mstr2+=lst2[i]
        else:
            mstr1+=lst1[i]
            mstr2+=lst2[i]

    if mstr1 == "":
        print("YODA")
        print(int(mstr2))
    elif mstr2 == "":
        print(int(mstr1))
        print("YODA")
    else:        
        print(int(mstr1))
        print(int(mstr2))
            



def main():
    #read input
    ip1 = str(input())
    ip1 = [i for i in ip1]
    ip2 = str(input())
    ip2 = [i for i in ip2]

    #check if the list sizes are the same - if not, we need to add 0s to the start of the number
    if len(ip1) == len(ip2):
        driver(ip1, ip2)
    else:
        smallerList = findSmallerList(ip1, ip2)
        biggerList = findBiggerList(ip1, ip2)
       
        newSmallerList = add0s(smallerList, max(len(smallerList),len(biggerList)))
        #print(newSmallerList)
        #print(biggerList)
        #call our driver
        driver(biggerList, newSmallerList)


if __name__ == "__main__":
    main()