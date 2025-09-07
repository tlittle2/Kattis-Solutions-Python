def main():
    vowels = ('a','e','i','o','u')
    s = input()

    ans = len(''.join(i for i in list(s) if i in vowels))

    print("{} {}".format(ans, ans + s.count('y')))

if __name__ == "__main__":
    main()
