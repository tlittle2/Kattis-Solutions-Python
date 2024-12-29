def main():
    n = int(input())

    ipList = [input() for _ in range(n)]

    if ipList == sorted(ipList):
        print("INCREASING")
    elif ipList == sorted(ipList, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")

    
if __name__ == "__main__":
    main()
