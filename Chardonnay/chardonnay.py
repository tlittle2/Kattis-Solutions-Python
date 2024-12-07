def main():
    ip = int(input())
    if ip == 0:
        print(0)
    else:
        print(ip + 1 if ip != 7 else 7)

if __name__ == "__main__":
    main()
