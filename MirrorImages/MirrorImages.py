#usr/bin/env python3

def main():
    numOfTestCases= int(input())

    for m in range(1, numOfTestCases+1):
        print("Test " + str(m))
        rows, cols= map(int, input().split())
        rInput=[]

        for i in range(rows):
            rInput.append(input())


        for j in reversed(rInput):
            print(j[::-1])

if __name__ == "__main__":
    main()