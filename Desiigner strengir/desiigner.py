def main():
    word = input()

    vowels = ['a','e','i','o','u', 'y']

    print('Jebb' if word[0] == 'b' and (word[1] == 'r' and word.count('r') > 1) and (word[len(word)-1] in vowels and word[len(word)-2] not in vowels) else 'Neibb')


if __name__ == "__main__":
    main()
