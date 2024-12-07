def main():
    days = [input() for _ in range(int(input()))]

    ans = 0
    for i in range(len(days)):
        if days[i] == "drunk" and days[i+1] == "sober":
            ans+=1
    
    print(ans)

if __name__ == "__main__":
    main()
