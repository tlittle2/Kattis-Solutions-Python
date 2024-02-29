def main():
    firstLine = list(map(str, input().split("|")))
    secondLine = list(map(str, input().split("|")))

    print("{}{} {}{}".format(firstLine[0], secondLine[0], firstLine[1], secondLine[1]))

if __name__ == "__main__":
    main()
