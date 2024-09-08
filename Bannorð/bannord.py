def main():
    badCharacters = list(input())
    sentence = input().split()

    for i in range(len(sentence)):
        for j in list(sentence[i]):
            if j in badCharacters: # if current character is bad character, update all characters in original word list to all *'s
                sentence[i] = "*" * len(sentence[i])
                break
    
    for word in sentence:
        print(word, sep= " ", end = " ")
    
if __name__ == "__main__":
    main()
