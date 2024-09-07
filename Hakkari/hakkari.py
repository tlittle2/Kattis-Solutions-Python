def main():
    rows, columns = map(int, input().split())
    lst = []

    for _ in range(rows):
        lst.append(list(input()))

    print(sum(row.count('*') for row in lst))

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '*':
                print(i+1,j+1)

if __name__ == "__main__":
    main()
