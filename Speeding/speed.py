#/bin/usr/env python3


def main():
    n = int(input())

    lst = []
    
    #set the initial time and distance to go off of (this will alway be 0,0 at the start and will be updated each time)
    initialTime, initialDist= map(int,input().split())
    
    # doing n - 1 because we don't need to account for the 0,0 case. We have already done it in the previous step 
    for i in range(n-1):
        newTime, newDist=map(int,input().split())
        
        #the speed will be the new - the initial because we are trying to calculate speed from 
        #   based off a window of 2 adjacent pictures at a time
        speed = (newDist - initialDist) / (newTime - initialTime)
        lst.append(int(speed))

        #set the new initials to the current new so that we can calculate our next window
        initialDist = newDist
        initialTime = newTime

    
    #because there can be cases where we will slow down, and we only want the max, we need to only update the max when
        # a new value is strictly greater than the current max
    max = 0
    for i in lst:
        if i > max:
            max = i

    print(max)


if __name__ == "__main__":
    main()