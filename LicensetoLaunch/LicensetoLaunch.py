#/usr/bin/env python3

def main():
    n= int(input())

    for i in range(0,n):

        m= (input().split())
        print(m)
    
        smallestValue= m[0]
        if m[i] < smallestValue:
            smallestValue= m[i]
        print(i)

if __name__ == "__main__":
    main()