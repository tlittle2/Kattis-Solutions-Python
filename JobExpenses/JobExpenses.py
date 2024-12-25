def main():
    int(input())
    total = 0
    values= []

    for i in input().split():
        values.append(i)

    for i in range(len(values)):
        if int(values[i]) < 0:
            total += int(values[i])

    print(total - total - total)
    
if __name__ == "__main__": 
    main()
