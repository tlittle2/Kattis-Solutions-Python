def main():
    n = int(input())

    ipList = [input() for _ in range(n)]

    print("INCREASING" if ipList == sorted(ipList) else "DECREASING" if ipList == sorted(ipList, reverse=True) else "NEITHER")

if __name__ == "__main__":
    main()
