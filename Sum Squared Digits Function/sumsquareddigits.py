def main():
    cases = int(input())

    for _ in range(cases):
        thiscase, base, num = map(int, input().split())
        sum = 0

        while num > 0:
            modulo = num % base
            sum += int(modulo * modulo)
            num = (num - modulo) / base

        print(str(thiscase) + " " + str(sum))

if __name__ == "__main__":
    main()
