#!/usr/bin/env python3

def split(a, n):
    #find the number of teams we should split into that would yield the most evenly distributed teams
    k, m = divmod(len(a), n)
    
    #use range() in such a way in order to figure out which part of the range should go into each room
        # do this because we can subtract the minimum and the maximum part of the range to figure out how many are going to be in each room (add 1 to this value because 
        # of indexing)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def main():
    rooms = int(input())
    teams = int(input())


    lst = (list(split(range(teams), rooms)))

    for i in lst:
        #store the number of stars into a variable so that we can use clever python string multiplication (add 1 because of 0-indexing)
        numOfStars= max(i) - min(i) + 1
        print(numOfStars * "*")





if __name__ == "__main__":
    main()