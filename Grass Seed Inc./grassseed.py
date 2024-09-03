def main():
    sum= 0
    const = float(input())
    numOfIn= int(input())
    
    for _ in range(numOfIn):
        num1, num2 = map(float,input().split())
        sum += num1 * num2

    answer = sum * const

    print(float(answer))

if __name__ == "__main__":
    main()
