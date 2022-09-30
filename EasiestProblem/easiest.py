#/usr/bin/env python3

#read input 'n'

#find the sum of digits of the input
#loop going from 2 until we find a number 'o'
    #if sum of digits n * o == sum of digits of input, print out number
    

def getSum(m):    
    sum = 0
    for digit in str(m): 
      sum += int(digit)      
    return sum 

def main():
    while True:
        n = int(input())
        if n == 0:
            break

        nSum = getSum(n)
        
        for i in range(11,100000,1):
            p = n * i
            #print("Number we are trying is {}".format(p))
            pSum= getSum(p)
            #print("The sum of the digits for {} is {}".format(p, pSum))
            if nSum == pSum:
                print(i)
                break






if __name__ == "__main__":
    main()