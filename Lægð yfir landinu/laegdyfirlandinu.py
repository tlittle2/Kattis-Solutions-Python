def comp(a,b):
    if (a < b):
        return True
    return False

def main():   
    rows, columns = map(int, input().split())

    lst = []
    for _ in range(rows):
        lst.append(list(map(int, input().split())))
    
    lp = False
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if comp(lst[i][j],lst[i+1][j]) and comp(lst[i][j],lst[i-1][j]) and comp(lst[i][j],lst[i][j+1]) and comp(lst[i][j],lst[i][j-1]):
                lp = True
                break    
    
    print("Jebb" if lp else "Neibb")


if __name__ == "__main__":
    main()
