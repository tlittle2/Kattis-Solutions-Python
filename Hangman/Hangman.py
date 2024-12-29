def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def main():    
    word= input().strip()
    letters = input().strip()

    wordList = [i for i in word]
    letterList = [i for i in letters]
    strikes = 0

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
