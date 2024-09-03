def main():
    count = 0
    for _ in range(int(input())):
        word = input().strip().lower()

        if "pink" in word or "rose" in word:
            count+=1

    print( "I must watch Star Wars with my daughter" if count == 0 else count)

if __name__ == "__main__":
    main()
