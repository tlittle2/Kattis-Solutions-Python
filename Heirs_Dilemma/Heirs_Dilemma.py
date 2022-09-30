#/usr/bin/env python3
#Trevor Little, Ben Mason

import time

start_time = time.time()
end_time = time.time()



globalCount=0

number, end= input().split()

number= int(number)
end= int(end)

global listOfValues

listOfValues= list(str(number))

def possibleValue():
        digitCount= [0,0,0,0,0,0,0,0,0,0]      
        for i in listOfValues:
                if(i==0):    
                    return False
                if(number % i!= 0):
                        return False
                digitCount[i]+=1
                #for j in range(i+1, 6):
                        #if(listOfValues[i] == listOfValues[j]):
                           #return False
        for i in range(10):
                if digitCount[i] > 1:
                   return False
        return True
                
while number <= end:
        if number % 2== 1:
                number+=1
        #listOfValues= list(str(number))
        temp = number
        for i in range(0, 6):
                listOfValues[i]= int(temp % 10)
                temp=temp/10
 

        if(possibleValue()):
                globalCount+=1
        number+=2

print(globalCount)