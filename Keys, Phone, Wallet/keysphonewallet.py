def main():
    n = int(input())

    things = {"keys", "phone", "wallet"}
    items = set()

    for _ in range(n):
        items.add(input())
    
    
    missing = sorted(list(things.difference(items)))
    
    if len(missing) == 0:
        print("ready")
    else:
        for i in missing:
            print(i)


if __name__ == "__main__":
    main()
