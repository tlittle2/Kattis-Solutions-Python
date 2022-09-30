#/usr/bin/env python3

import sys

def main(): 
    numOfLocations= int(sys.stdin.readline())
    numOfItems= list(map(int, sys.stdin.readline().split()))
    numOfRoads= int(sys.stdin.readline())

    cost= []

    def minDistance(distance, sptSet):
        min = sys.maxsize
        min_index= 0
        for v in range(numOfLocations):
            if distance[v] < min and sptSet[v]==False:
                min= distance[v]
                min_index= v
        return min_index



    for i in range(numOfLocations):
        cost.append(numOfLocations * [0])

        
    for i in range(numOfRoads):
        start, end, distance= list(map(int, sys.stdin.readline().split()))
        cost[start-1][end-1]= distance
        cost[end-1][start-1]= distance

    newDistance= numOfLocations * [sys.maxsize]
    newDistance[0]=0


    numOfPackages= numOfLocations * [0]
    numOfPackages[0]=numOfItems[0]


    validPath= numOfLocations * [False]
    validPath[0]= True



    for _ in range(numOfLocations):
        startingPoint= minDistance(newDistance, validPath)
        validPath[startingPoint]= True
        for i in range(numOfLocations):
            if(cost[startingPoint][i] > 0 and validPath[i] == False):
                if newDistance[i] > (cost[startingPoint][i] + newDistance[startingPoint]):
                    newDistance[i] = cost[startingPoint][i] + newDistance[startingPoint]
                    numOfPackages[i]= numOfItems[i] + numOfPackages[startingPoint]
                elif newDistance[i] == (cost[startingPoint][i] + newDistance[startingPoint]):
                    if numOfPackages[i] < numOfItems[i] + numOfPackages[startingPoint]:
                        numOfPackages[i]= numOfItems[i] + numOfPackages[startingPoint]

    if (newDistance[-1] == sys.maxsize):
        print("impossible")
    else:
        print(newDistance[-1], numOfPackages[-1], sep= ' ')

if __name__ == "__main__":
    main()