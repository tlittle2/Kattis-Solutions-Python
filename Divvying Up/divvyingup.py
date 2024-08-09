def main():
    c = int(input())
    money = list(map(int, input().split()))

    if sum(money) % 3 == 0:
        print("yes")
    else:
        print("no")
    

if __name__ == "__main__":
    main()
