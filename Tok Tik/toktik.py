def main():
    m = dict()
    n = int(input())

    for i in range(n):
        line = input().split()
        
        if line[0] in m: #if name is in map, add to the number of views for that key, else add entry to the map
            m[line[0]]+= int(line[1])
        else:
            m[line[0]]= int(line[1])

    print(max(m, key=m.get)) # print key that has the max integer value

if __name__ == "__main__":
    main()
