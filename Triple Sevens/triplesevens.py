def main():
    n = int(input())

    l = list()

    for _ in range(3):
        for num in list(map(int, input().split())):
            l.append(num)

    if l.count(7) == 3:
        print(777)
    else:
        print(0)
    


if __name__ == "__main__":
    main()
