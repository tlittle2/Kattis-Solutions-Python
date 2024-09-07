def main():
    wind = int(input())
    for _ in range(int(input())):
        ip = input().split()
        if int(ip[1]) < wind:
            print("{} lokud".format(ip[0]))
        else:
            print("{} opin".format(ip[0]))

if __name__ == "__main__":
    main()
