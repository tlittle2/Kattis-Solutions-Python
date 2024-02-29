def main():
    firstLine = list(map(int, input().split()))

    maxWeight = (firstLine[0] - firstLine[1])* 0.9

    weights = list(map(int, input().split()))

    s = sum(weights)

    print(int(maxWeight -s))

if __name__ == "__main__":
    main()
