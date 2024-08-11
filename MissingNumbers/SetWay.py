def main():
    n= int(input())
    numList = set()
    for _ in range(n):
        numList.add(int(input()))
    
    master = {i for i in range(1,max(numList))} #create set from 1 to the max of our list

    diff = master.difference(numList) #find differences in the sets

    if len(diff) == 0:
        print("good job")
    else:
        for i in sorted(list(diff)):
            print(i)

if __name__ == "__main__":
    main()
