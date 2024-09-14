def main():
    values = list(map(int, input().split()))
    
    if sum([int(input()) for _ in range(values[0])]) <= values[1]:
        print("Jebb")
    else:
        print("Neibb")

if __name__ == "__main__":
    main()
