def main():
    lst = []
    lp = False

    rows, columns = map(int, input().split())

    for _ in range(rows):
        lst.append(list(map(int, input().split())))

    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if lst[i][j] < lst[i+1][j] and lst[i][j] < lst[i-1][j] and lst[i][j] < lst[i][j+1] and lst[i][j] < lst[i][j-1]:
                lp = True
                break

    print("Jebb" if lp else "Neibb")

if __name__ == "__main__":
    main()
