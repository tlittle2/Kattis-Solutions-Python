def main():
    _ =input().split()

    ip1 = list(map(int, input().split()))
    ip2 = list(map(int, input().split()))

    seen = set()

    ordered_unique = []

    for i in ip1:
        if i not in seen and i in ip2:
            seen.add(i)
            ordered_unique.append(i)
    
    for i in ordered_unique:
        print(i, sep = " ", end =" ")

if __name__ == "__main__":
    main()
