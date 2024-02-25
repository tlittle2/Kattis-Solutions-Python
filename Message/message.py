def main():
    s = ""
    l = list()
    rows,length= map(int, input().split())


    for i in range(rows):
        l.append(input().split())

    
    #print(l)

    for i in range(len(l)):
        for j in range(len(l[i])):
            for k in range(len(l[i][j])):
                if l[i][j][k] != '.':
                    s += l[i][j][k]
                    
    print(s)




if __name__ == "__main__":
    main()
