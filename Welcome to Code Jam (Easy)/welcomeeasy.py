def counter(testcase, start=0):
    codeJam= 'welcome to code jam'
    codeJamLength= len(codeJam)
    numOfCorrect= 0
    
    #Base case
    if start== codeJamLength-1:
        for i in testcase:
            if i == 'm':
                numOfCorrect+=1
        return numOfCorrect

    #Recursive case
    for i in enumerate(testcase):
        if i[1]== codeJam[start]:
            numOfCorrect+= counter(testcase[i[0] + 1:], start+1)
    return numOfCorrect

def main():
    for i in range(int(input())):
        numOfOccurrences= counter(input())
        print("Case #",i+1, ": %04d" % numOfOccurrences, sep= "")
    
if __name__ == "__main__":
    main()
