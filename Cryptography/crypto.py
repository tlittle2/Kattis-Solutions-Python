#!/usr/bin/env python3

from string import ascii_uppercase as upp

def main():
    message = str(input())
    mLst = [str(i) for i in message]
    key = str(input())
    kLst = [str(i) for i in key]

    for i in range(len(kLst)-1, -1, -1):
        mLst.pop(len(mLst)-1)
        mLst.insert(0,kLst[i])

    print("new word: {}".format(mLst))
    print(len(mLst))

    for i in range(len(kLst), len(mLst)):
        print("{} {} ".format(i, mLst[i]))
        print("{} - {}".format(upp.index(mLst[i]), upp.index(kLst[i % len(kLst)])))
        new = upp.index(mLst[i]) - upp.index(kLst[i % len(kLst)])
        print("new Letter: {}".format(upp[new]))
        print()





if __name__ == "__main__":
    main()