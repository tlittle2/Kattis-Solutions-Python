def main():
    cases = int(input())
    ans = 0
    for _ in range(cases):
        if int(input()) % 2 !=0:
            ans+=1
    print(ans)

if __name__ == "__main__":
    main()
