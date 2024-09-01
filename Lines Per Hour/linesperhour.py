def main():
    n, lph = map(int, input().split())

    l = sorted([int(input()) for _ in range(n)])
    l.append(25001) # for some reason, adding a big number to the end of the problem removed run-time error
    
    total = 5 * lph
    solved = -1 #start at -1 just in case we happen to not be able to solve any problems

    while total >= 0:
        total -= l.pop(0)
        solved+=1

    print(max(solved,0))


if __name__ == "__main__":
    main()
