#/usr/bin/env python3
import sys


def harshad(someNum):

    #print("trying + " + str(someNum))
    list = [int(i) for i in str(someNum)]
    sum= 0
    #print(list)

    for i in range(len(list)):
        sum += list[i]

   # print("Sum after traverse" + str(sum))

    if someNum % sum == 0:
        print(someNum)
    else:
        someNum +=1
        harshad(someNum)



def main():
    num = int(sys.stdin.readline())
    harshad(num)


if __name__ == "__main__":
    main()