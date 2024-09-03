def main():
    _, _= map(int, input().split())

    array= list(map(int, input().split()))

    counts= []

    checked= []
    for i in array:
        if checked.count(i) == 0:
            counts.append([i, array.count(i)])
            checked.append(i)
            #print(counts)

    counts= sorted(counts, key= lambda x: x[1], reverse= True)

    for count in counts:
        for _ in range(count[1]):
            print(count[0], end= " ")

if __name__ == "__main__":
    main()
