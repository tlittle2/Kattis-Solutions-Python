def main():
    a,b = map(int, input().split())
    
    aCopy = a
    a= a*(a+1)//2
    a%=aCopy

    ans = 1
    
    while(b > 0):
        ans = ans * a % aCopy
        a*= a % aCopy
        b>>=1 #bitwise shift by 1

    print(ans)

if __name__ == "__main__":
    main()
