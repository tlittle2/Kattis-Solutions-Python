#/usr/bin/env python3

codeJam= 'welcome to code jam'

def counter(testcase, start=0):
    numOfCorrect= 0
#Base case
    if start== (len(codeJam)-1):
        for i in testcase:
            if i == 'm':
                numOfCorrect+=1
        return numOfCorrect
#Recursive case
    for i in enumerate(testcase):
        if i[1]== codeJam[start]:
            numOfCorrect+= counter(testcase[i[0] + 1:], start+1)
    return numOfCorrect



numOfTestCases= int(input())

for i in range(numOfTestCases):
    numOfOccurrences= counter(input())
    print("Case #",i+1, ": %04d" % numOfOccurrences, sep= "")