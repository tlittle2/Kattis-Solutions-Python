def main():
    array= []

    numOfCups= int(input())

    for _ in range(numOfCups):
        ip1, ip2 = input().split()

        if ip1.isnumeric()== True:  
            array.append([int(ip1),ip2])
        else:
            array.append([int(ip2) * 2, ip1])
        
        array= sorted(array)

    for i in array:
        print(i[1])
        
if __name__ == "__main__":
    main()
