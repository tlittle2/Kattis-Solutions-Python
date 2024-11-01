def main():
    ip = int(input())

    print(sum(i for i in range(1,ip+1)))
    print(sum(sum([j for j in range(1,i+2)]) for i in range(ip)))

if __name__ == "__main__":
    main()
