#/usr/bin/env python3

import sys

def main():
    #numOfTestCases= int(sys.stdin.readline())
    while True:
        speed= int(sys.stdin.readline())
        if speed== -1:
            break


        total= 0
        endTime= 0
        currentSpeed= 0
        currentTime= 0

        for i in range(speed):
            currentSpeed= int(sys.stdin.readline(), end= "")
            currentTime= int(sys.stdin.readline())
            total+= (currentTime- endTime) * currentSpeed
            endTime= currentTime

        print(total + " miles")

if __name__ == "__main__":
    main()