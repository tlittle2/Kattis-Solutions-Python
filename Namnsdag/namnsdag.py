def main():
    name = input()

    num = int(input())
    ans = num-1

    comparors = [input() for _ in range(num)]

    for i in range(1,num):
        currName = comparors[i]

        if len(currName) == len(name):
            diff = sum(1 for a,b in zip(name, currName) if a!=b) #get the number of times where masterName[i] is not equal to currName[i]
            if diff == 1: #if that difference is exactly 1, then update our answer
                ans = min(ans, i)

    print(ans+1)
                
if __name__ == "__main__":
    main()
