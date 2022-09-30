#!/bin/usr/env python3

def main():
    # Make a list of integers from the input (there was no real easy way to do this because of the nature of the input)
    numString = input()
    num = numString.split()
    m= map(int, num)
    numList = list(m)
    
    # Real logic starts here
    numList = sorted(numList)

    letters= list(i for i in input())

    answer = ""
    
    for i in range(3):
        if letters[i] == 'A':
            answer+="{} ".format(numList[0])
        elif letters[i] == 'B':
            answer+="{} ".format(numList[1])
        elif letters[i] == 'C':
            answer+="{} ".format(numList[2])

    print(answer)



if __name__ == "__main__":
    main()