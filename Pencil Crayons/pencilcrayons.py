def main():
    boxes, _ = map(int, input().split())

    count = 0
    for _ in range(boxes):
        colors = input().split()
        s = set(colors)
        count+= len(colors) - len(s)

    print(count)

if __name__ == "__main__": 
    main()
