def main():
    _ = int(input())
    lines = int(input())
    lst = []

    for _ in range(lines):
        for k in list(input()):
            lst.append(k)

    print(1-(lst.count('#') / len(lst)))    

if __name__ == "__main__":
    main()
