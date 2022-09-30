#!/usr/bin/env python3
from string import ascii_uppercase

def main():
    letters = [i for i in ascii_uppercase]
    
    message = input()
    key = input()

    new = ""


    for i in range(len(message)):
        l = ""
        if i % 2 == 0:
            idx = letters.index(message[i]) - letters.index(key[i])
            l = letters[idx % 26]
        else:
            idx = letters.index(message[i]) + letters.index(key[i])
            l = letters[idx % 26]
        new +=l
    
    print(new)


if __name__ == "__main__":
    main()