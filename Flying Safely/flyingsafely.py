def main():
    numOfCases= int(input())
    for _ in range(numOfCases):
        numOfCities, numOfPilots= map(int, input().split())
        for _ in range(numOfPilots):
            _, _= map(int, input().split())
        print(numOfCities-1)

if __name__ == "__main__":
    main()
