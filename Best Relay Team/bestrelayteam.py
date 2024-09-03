def main():
    numOfCases= int(input())
    runnerList= []

    for _ in range(numOfCases):
        name, standing, handoff= input().split()
        runnerList.append([name, float(standing), float(handoff)])

    standingList= sorted(runnerList, key= lambda x: x[1])
    handoffList= sorted(runnerList, key= lambda x: x[2])

    standingList= standingList[0:4]
    handoffList= handoffList[0:4]

    bestTime= -1

    runnerOrder= []
    for runner in standingList:
        time= runner[1]
        runnerOrder= [runner[0]]
        count = 0
        for nextRunner in handoffList:
            if count > 2:
                break
            if runner[0] == nextRunner[0]:
                continue
            else:
                time+= nextRunner[2]
                runnerOrder.append(nextRunner[0])
            count+=1
        if bestTime > time or bestTime== -1:
            bestTime = time
            fastestOrder= runnerOrder
    print(bestTime)
    for runner in fastestOrder:
        print(runner)    
    
if __name__ == "__main__":
    main()
