#!/usr/bin/env python3


#THIS SOLUTION ONLY WORKS FOR THE SAMPLE INPUT

def sortDict(d):
    dList =  sorted(d.items(), key=lambda x:x[1], reverse= True)
    finalDict = dict(dList)
    return finalDict



def main():
    cases = int(input())

    for i in range(cases):
        n = int(input())
        
        finalList = []
        upperDict = {}
        midDict =  {}
        lowerDict = {}
        
        for i in range(n):
            #split the input so we don't have the word "class"
            s = input().split(": ")

            classSplit = s[1].replace("class", "")

            #put counts of all inputs as key-value pairs of a dictionary (key = name, value = count)
            upperDict[s[0]] = classSplit.count("upper")
            midDict[s[0]] = classSplit.count("middle")
            lowerDict[s[0]] = classSplit.count("lower")
            
        #sort the dictionary keys in reverse order for easier lookup
        sortedUpper = sortDict(upperDict)
        sortedMid = sortDict(midDict)
        sortedLower = sortDict(lowerDict)

        #append values to final list based on conditions
        for k, v in sortedUpper.items():
            if k not in finalList and v !=0:
                finalList.append(k)

        
        for k, v in sortedMid.items():
            if k not in finalList and v !=0:
                finalList.append(k)


        for k, v in sortedLower.items():
            if k not in finalList and v !=0:
                finalList.append(k)
        

        for i in finalList:
            print(i)

        
        print("==============================")






if __name__ == "__main__":
    main()