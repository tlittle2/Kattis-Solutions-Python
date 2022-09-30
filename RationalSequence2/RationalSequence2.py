#/usr/bin/env python3

def traversal(numerator, denominator):
    if numerator==1 and denominator==1:
        return 1
    elif numerator> denominator:
        return traversal(numerator, denominator - numerator)
        #return traversal(numerator*2, denominator)
    elif numerator < denominator:
        return traversal(numerator - denominator), denominator
        #return traversal(numerator *2, denominator +1) 
    
def main():

    numOfCases= input()

    for i in range(numOfCases):
        dataNumber, rational= input().split()
        numerator, denominator= map[int, numerator, denominator]

if __name__ == "__main__":
    main()