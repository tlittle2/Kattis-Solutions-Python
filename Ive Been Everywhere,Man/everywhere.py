def main():   
    n = int(input())

    for _ in range(n):
        s = set()
        cities = int(input())
        for _ in range(cities):
            s.add(input())

        print(len(s))

if __name__ == "__main__":
    main()
