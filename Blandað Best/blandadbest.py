def main():
    s = set()

    n = int(input())

    for i in range(n):
        s.add(input())

    if len(s) == 2:
        print("blandad best")
    else:
        for i in s:
            print(i)
    
if __name__ == "__main__":
    main()
