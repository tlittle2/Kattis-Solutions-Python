import math
def main():
    n, k= map(int, input().split())
    out= 1

    times=[0]*n

    first= 0
    temp= 1

    times[0]= int(input())

    for i in range(1, n):
        times[i]= int(input())
        while(times[first] + 1000 <= times[i]):
            first+=1
            temp-=1
        temp+=1
        out= max(out,temp)

    print(int(math.ceil(1.0 * out / k)))
    
if __name__ == "__main__":
    main()
