#/usr/bin/env python3

#Trevor Little
'''
This solution was not accepted by Kattis due to a Time Limited Exceeded Error.
I have tried 3 different solution, none of which have been fast enough.
The reason for this I believe is because it takes too long on the count function
when you have a large range of 1 bits.
'''


bits, operations= input().split()

global IndexesChanged
IndexesChanged= 1000000 * [0]

def split_search(a, start, end):
    numOfOnes=0
    if len(a[start:end+1]) <= 3:
        numOfOnes= a[start:end+1].count(1)

    else:        
        midPoint= int(end/2)+int(start/2)
        numOfOnes+=split_search(a, start, midPoint)
        numOfOnes+=split_search(a, midPoint+1, end)
    return numOfOnes
           

def flip(fPosition):
            IndexesChanged[fPosition]= 1-IndexesChanged[fPosition]


def count(start, end):
            print(split_search(IndexesChanged, int(start), int(end)))
        
       
for j in range(0, int(operations)):
    inthing= input().split()
    typeOfOperation= inthing[0]
    if typeOfOperation== 'F':
        flip(int(inthing[1]))
    elif typeOfOperation== 'C':
        count(int(inthing[1]), int(inthing[2]))