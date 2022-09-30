#/usr/bin/env python3

def main():
    a,b= map(int, input().split())

    m, theta= map(int, input().split())

    start= 0


    rMax= 0

    if (theta-m) > 1:
        start= theta-m

    else:
        start= 1


    if a-b > 0:
        rMax= (a-b)*(m-1)+(b*m)

    elif theta-m > 1:
        rMax= (a-b)*(theta-m)+ b*m

    else:
        rMax= (a-b)*1+ b*m

    '''
    for x in range(start, (m-1)+1, 1):
        r= ((a-b) * x) + b*m
        if r > rMax:
            rMax= r
    '''
    print(rMax)

if __name__ == "__main__":
    main()