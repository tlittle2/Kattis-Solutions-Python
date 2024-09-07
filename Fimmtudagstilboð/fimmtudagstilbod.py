def main():
    year = int(input())
    if year < 2020:
        print(1000)
    else:
        print(((year - 2020) * 100) + 1000)

if __name__ == "__main__":
    main()
