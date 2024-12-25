def main():
    _ =input().split()

    ip1 = list(map(int, input().split()))
    ip2 = list(map(int, input().split()))

    seen = []

    for i in ip1:
        if i not in seen and i in ip2:
            seen.append(i)
    
    for i in seen:
        print(i, sep = " ", end =" ")

if __name__ == "__main__":
    main()
