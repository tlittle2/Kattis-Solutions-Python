import string
def main():
    print(len([x for x in list(input()) if x in string.ascii_uppercase or x in string.ascii_lowercase]))

if __name__ == "__main__":
    main()
