def main():
    l = []

    _ = input()
    percent = float(input())
    ips = int(input())

    for _ in range(ips):
        l.append(input())

    if l.count("ekki plast") / ips <= percent:
        print("Jebb")
    else:
        print("Neibb")

if __name__ == "__main__":
    main()
