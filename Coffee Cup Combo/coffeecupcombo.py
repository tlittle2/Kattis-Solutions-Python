def main():
    classes = int(input())
    s = input()

    sum = 0

    tempSum = 0
    for i in range(len(s)):
        if(s[i] == '1'):
            tempSum = 2
            sum+=1

        else:
            if tempSum > 0:
                sum+=1
            tempSum-=1

    print(sum)
    
if __name__ == "__main__":
    main()
