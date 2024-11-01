def main():
    ip = int(input())

    print(sum(i for i in range(1,ip+1)))

    s = 0
    for i in range(ip):
        s+= sum([j for j in range(1,i+2)])

    print(s)

if __name__ == "__main__":
    main()
