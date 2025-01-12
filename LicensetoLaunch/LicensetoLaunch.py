def main():
    int(input())
    values = list(map(int, input().split()))

    d = {i: values[i] for i in range(len(values))}

    print(min(d, key=d.get))

if __name__ == "__main__":
    main()
