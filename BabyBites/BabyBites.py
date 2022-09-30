#/usr/bin/env python3


import sys

def main():
    mumble= "mumble"

    wordOrNot= True

    numOfBites= int(sys.stdin.readline())
    word= sys.stdin.readline().split()
    count= len(word)

    for i in range(0, count):
        #print(i, word[i])
        if word[i]==str(i+1)or word[i]== mumble:
            pass
        else:
            wordOrNot= False
            break


    if wordOrNot== True:
        print("makes sense")
    else:
        print("something is fishy")

if __name__ == "__main__":
    main()