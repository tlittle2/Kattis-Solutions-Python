#/usr/bin/env python3
#this implementation does things in the order in which the letters are given in the second input
import sys

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def main():
    wordList= []
    letterList = []


    strikes = 0
    found = 0

    word= sys.stdin.readline().strip()
    letters = sys.stdin.readline().strip()

    for i in word:
        wordList.append(i)
    for i in letters:
        letterList.append(i)


    for c in letterList:
        if wordList.count(c):
            wordList = remove_values_from_list(wordList, c)
            if len(wordList) == 0:
                print("WIN")
                break

        else:
            strikes += 1
            if strikes == 10:
                print("LOSE")
                break
if __name__ == "__main__":
    main()