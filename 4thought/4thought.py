#!/bin/usr/env python3


def main():
    #make set of operators
    #make sure they have spaces, it is important to the output
    operators = (' // ', ' * ', ' - ', ' + ')
    
    #we will store the values answer and the equation into a dictionary for easy lookup
    dict = {}

    #get all possible combinations of operators and put each into a dictionary
    #do triple for loop to account for all operators accept for a repeat of the last one
    #use the eval function to help evaluate a math equation based on string input
    for i in operators:
        for j in operators:
            for k in operators:
                v = "4{}4{}4{}4".format(i,j,k)
                val = eval(v)
                dict[val] = v.replace('//', '/') + " = {}".format(val)

    #we need to narrow the search space before trying to compute an answer
        #if the value we are trying to find is not in the dictionary, then there is no solution
        #if the value is greater than 256 (the largest value in our dictionary), the number cannot be reached
        #if the value is less than -60 (the smallest number in our dictionary), the number cannot be reached
    
    for i in range(int(input())):
        n = int(input())
        if n < -256 or n > 256 or n not in dict:
            print("no solution")
        else:
            print(dict[n])
    

if __name__ == "__main__":
    main()