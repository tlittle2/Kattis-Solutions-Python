def main():
    ip = list(input())

    result = []

    for char in ip:
        if not result or result[-1] != char: # if list is empty or the result at the current last index is the same as the current character
            result.append(char)

    print(''.join(result))

if __name__ == "__main__":
    main()
