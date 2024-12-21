def main():
    boxes, _ = map(int, input().split())

    count = 0
    for _ in range(boxes):
        colors = input().split()
        count+= len(colors) - len(set(colors))

    print(count)

if __name__ == "__main__": 
    main()
