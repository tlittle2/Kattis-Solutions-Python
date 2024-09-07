def main():
    _ = int(input())
    lst = []
    for _ in range(int(input())):
        for k in list(input()):
            lst.append(k)

    print(1-(lst.count('#') / len(lst)))    

if __name__ == "__main__":
    main()
