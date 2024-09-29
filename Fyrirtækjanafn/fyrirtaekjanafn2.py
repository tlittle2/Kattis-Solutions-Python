def main():
    vowels = "aeiouyAEIOUY"
    print(''.join([char for char in input() if char in vowels or char.isspace()]))

if __name__ == "__main__":
    main()
