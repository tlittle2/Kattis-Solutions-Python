import sys, math
def main():
    vArray= []

    numOfQueries= int(sys.stdin.readline())

    temp= list(map(float, sys.stdin.readline().split()))

    vArray= temp[0:numOfQueries]
    b= temp[-1]


    while(True):
        ip= sys.stdin.readline()
        if ip == "" or ip == "\n":
            break
        xArray= list(map(float, ip.split()))
        runningTotal= 0
        for i in range(numOfQueries):
            runningTotal += (vArray[i] * xArray[i]) 
        runningTotal+=b
        magnitude= 0
        for i in range(numOfQueries):
            magnitude+= vArray[i] * vArray[i]
        magnitude= math.sqrt(magnitude)
        answer= runningTotal/ magnitude
        print("%.5f" % answer)
        
if __name__ == "__main__":
    main()
