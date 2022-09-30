#!/bin/usr/env python3

def main():
    nums, skip = map(int, input().split())
    
    #create master list with dummy first value (as one character only) in order to allocate for 1-indexing later
    master = list("n")
    
    #read in values and put them into a temporary list
    tempList = list(map(str, [i for i in input().split()]))

    #insert all values from the temporary list into the master one at a time
    for i in tempList:
        master.append(i)


    #read all values from the master list into a new list    
    vals = list()
    for i in range(0, len(master), skip):
        vals.append(master[i])

    #if the dummy value is in final list of values we will be printing out, make sure to remove it
    #if the dummy value is not there, EVEN BETTER (there is nothing to remove)
    if "n" in vals:
        vals.remove(vals[0])

    #print out all the values on the same line
    for i in vals:
        print(i, sep = " ", end = " ")


    




if __name__ == "__main__":
    main()