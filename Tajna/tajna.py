#!/usr/bin/env python3

import math

def divisibility(m):
    for i in range(int(math.sqrt(m)+.1), 1, -1):
        if m % i == 0:
            return i
    
    return m

def main():
    n = [i for i in input()]
    print(len(n))

    rows = divisibility(len(n))
    print(rows)
    columns = int(len(n) / rows)

    master = []

    tempN= 0
    for i in range(0, rows):
        temp = []
        for j in range(0, columns):
            temp.append(n[tempN])
            tempN+=1
        
        master.append(temp)


    print(master)
    

    for j in range(columns):
        #print(master[i])
        for i in range(rows):
            print(master[i][j], end="")


    '''
    USE THE LOOP ONCE YOU MANIPULATE THE ARRAYS CORRECTLY
    
    master = [['b','o', 'm', 'b'],['o','n', 'i', 's'],['u','u', 'l', 'a'],['d','i', 'c', 'i']]

    
    `for i in range(columns):
        #print(master[i])
        for j in range(rows):
            print(master[j][i], end="")`
    '''




if __name__ == "__main__":
    main()