def main():
    days = [input() for _ in range(int(input()))]

    print(sum(1 for i in range(len(days)) if days[i] == "drunk" and days[i+1] == "sober"))

if __name__ == "__main__":
    main()
