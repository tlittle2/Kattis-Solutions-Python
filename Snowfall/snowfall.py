def main():
    n = int(input())

    ans = 0
    for _ in range(n):
        t,a = map(int, input().split())
        
        ans = max(ans - a, 0) if t==1 else ans + a
            
    print(ans)

if __name__ == "__main__": 
    main()
