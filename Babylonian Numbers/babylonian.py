def main():
    for _ in range(int(input())):
        n = [0 if x == '' else int(x) for x in input().split(",")] #blanks are the equivalent to zeros in the number system
        d = len(n)-1
        s = 0
        for i in n:
            s+= i * 60**d
            d-=1
        print(s)
        
if __name__ == "__main__":
    main()
