def main():
    n = int(input())

    l = []

    for _ in range(n):
        si, ti = map(int, input().split())
        r = range(si, ti + 1)

        for j in r:
            if j not in l:
                l.append(j)

    print(len(l))


if __name__ == "__main__":
    main()
