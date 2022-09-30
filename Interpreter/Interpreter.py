#/usr/bin/env python3

import sys, math, functools, time

start_time= time.time()

end_time= time.time()

global registerList
global pointer
pointer= 0
registerList=[0,0,0,0,0,0,0,0,0,0]
global RAM
RAM= [0 for x in range(1001)]


def function1(x, y):
    return True

def function2(d, n):
    registerList[d]=n
   

def function3(d, n):
    registerList[d]+=n
    if registerList[d] > 999:
        registerList[d]= registerList[d] % 1000
    

def function4(d, n):
    registerList[d]*=n
    if registerList[d] > 999:
        registerList[d]= registerList[d] % 1000
    
    
def function5(d, s):
    registerList[d]= registerList[s]

def function6(d, s):
    registerList[d]+=registerList[s]
    if registerList[d] > 999:
        registerList[d]= registerList[d] % 1000
    
def function7(d, s):
    registerList[d]*=registerList[s]
    if registerList[d] > 999:
        registerList[d]= registerList[d] % 1000
    
def function8(d, a):
    registerList[d]=RAM[registerList[a]]
    

def function9(s, a):
    RAM[registerList[a]]= registerList[s]

j=0  
for i in sys.stdin:
    
    if i == "\n":
        break
    RAM[j]=int(i)
    j+=1

steps=0

for i in range(0,10001):
    steps+=1
    
    
    num2= RAM[pointer] % 10
    num1= (RAM[pointer] // 10) % 10
    operation= RAM[pointer] // 100 


    if operation== 1:
        if function1(num1, num2):
            break    
    elif operation==2:
        function2(num1, num2)
        pointer+=1
    elif operation==3:
        function3(num1, num2)
        pointer+=1
    elif operation==4:
        function4(num1, num2)
        pointer+=1
    elif operation==5:
        function5(num1, num2)
        pointer+=1
    elif operation==6:
        function6(num1, num2)
        pointer+=1
    elif operation==7:
        function7(num1, num2)
        pointer+=1
    elif operation==8:
        function8(num1, num2)
        pointer+=1
    elif operation==9:
        function9(num1, num2)
        pointer+=1
    elif operation==0:
        if registerList[num2] !=0:
            pointer= registerList[num1]
        else:
            pointer+=1

    #print(operation, num1, num2, registerList)
print(steps)
#print(end_time - start_time)
