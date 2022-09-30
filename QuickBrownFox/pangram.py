#!/usr/bin/env python3

from string import ascii_lowercase
from string import punctuation


def main():
    n = int(input())

    for i in range(n):
        missing = ""
        s = input()
        
        s = s.lower()

        for c in ascii_lowercase:
            if c not in s and c not in punctuation:
                missing+=c
    
    
        if len(missing) == 0:
            print("pangram")
        else:
            print("missing {}".format(missing))
        




if __name__ == "__main__":
    main()