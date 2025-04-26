def main():
    ip = input().split('?')

    a = int(ip[0].strip())
    b = int(ip[1].strip())

    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("Goggi svangur!")

if __name__ == "__main__":
    main()
