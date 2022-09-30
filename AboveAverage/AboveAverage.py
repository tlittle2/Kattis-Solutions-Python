#/usr/bin/env python3

import sys

numOfCases= int(sys.stdin.readline())
grades= " "
average=0

masterGrades=[]
masterAverage= []
for i in range(numOfCases):
    grades= list(map(int, sys.stdin.readline().split()))
    total= 0
    masterGrades.append(grades)
    for i in range(1, len(grades)):
        total+=grades[i]
        average= total / grades[0]
    masterAverage.append(average)


newAverage= 0
for i in range(numOfCases):
    avgStudents= 0
    for j in range(1, len(masterGrades[i])):
        if(masterGrades[i][j] > masterAverage[i]):
            avgStudents+=1
    newAverage= avgStudents/ masterGrades[i][0]
    print(("%5.3f"%(newAverage * 100 )+ '%'))