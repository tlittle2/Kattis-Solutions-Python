def main():
    for _ in range(int(input())):
        a, b, c= map(int, input().split())

        if a+ b ==c:
            print("Possible")
        elif a-b ==c or b-a==c:
            print("Possible")
        elif a * b== c:
            print("Possible")
        elif b/a==c or a / b==c:
            print("Possible")
        else:
            print("Impossible")

if __name__ == "__main__":
    main()
