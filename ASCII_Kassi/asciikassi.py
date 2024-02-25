def main():
    plus = '+'
    pipe = '|'

    n = int(input())

    print('{}{}{}'.format(plus, '-' *n, plus))
    for i in range(n):
        print('{}{}{}'.format(pipe, ' ' *n, pipe))

    print('{}{}{}'.format(plus, '-' *n, plus))

if __name__ == "__main__":
    main()
