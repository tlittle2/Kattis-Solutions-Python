def main():
    num = int(input())
    word = input().split()
    for i in word:
        if i[0].isupper():
            print(i[0], sep="", end="")
    
if __name__ == "__main__":
    main()
