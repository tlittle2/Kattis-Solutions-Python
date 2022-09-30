#/usr/bin/env python3
import sys

def main():
    n= int(sys.stdin.readline())

    correct= []

    myAnswers= []
    same= True

    count=0
    for i in range(n):
        answer= sys.stdin.readline()
        correct.append(answer)


    for i in range(1, len(correct)):
        myAnswers.append(correct[i])


    for i in range(len(correct) -1):
        if correct[i] == myAnswers[i]:
            count+=1

    print(count)

if __name__ == "__main__":
    main()