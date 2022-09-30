#/usr/bin/env python3
import sys

def splitFurther(indice):
    #print(indice)
    dash = 0
    for i in range(0, len(indice)):
        if indice[i] == '-':
            dash = i
            #print(dash)

    firstNumber = int(indice[0:dash])
    secondNumber = int(indice[dash+1::])

    #print("First Number: "+ str(firstNumber), "second Number: " + str(secondNumber))
    ourRange= secondNumber - firstNumber +1
    #print("The range here is: " + str(ourRange))
    return ourRange


def main():
    ourIn= sys.stdin.readline().strip()
    ourIn = ourIn.split(';')
    answer= 0

    #print(ourIn)

    for i in ourIn:
        if i.count('-') == 1:
           answer+= splitFurther(i)
        else:
            answer+=1
    print(answer)

if __name__ == "__main__":
    main()