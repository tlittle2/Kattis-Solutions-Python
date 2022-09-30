#/usr/bin/env

import math
import sys


def main():
    # Establish the factorials we need
    factorials = [math.factorial(i) for i in range(101)]

    for inp in sys.stdin:
        word = str(inp.split()[0])
        d = {}

        answer= 0

        for i in word:
            #if the character is already a key in the dictionary, add to the value, otherwise set it to 1
            if ord(i) in d:
                d[ord(i)] +=1
            else:
                d[ord(i)] = 1
        
        #Our original answer will be the factorial for the length of the word
        answer = math.factorial(len(word))
        
        # for each entry in our dictionary, we change our answer to be the integer division value of the previous answer and the factorial value 
        # for the number of occurrences of that digit 
        for i in d:
            answer = answer // factorials[d[i]]

        print(answer)

        # we have to do this step because the number can change as you go through the string if you have duplicates string sequences
            # Because we only want to count a string sequence once, we want to take away the amount of duplicates we could get for 
            #       a possible string sequence
            # By doing answer = answer // factorials[d[i]] we bypass duplication by getting the same answer without stopping
            # we don't want to stop because there could be strings later on down the line that need to be accounted for




if __name__ == "__main__":
    main()