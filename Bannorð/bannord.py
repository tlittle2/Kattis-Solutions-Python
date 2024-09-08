def main():
    badCharacters = list(input())
    sentence = input().split()

    for i in range(len(sentence)):
        for j in list(sentence[i]):
            if j in badCharacters:
                sentence[i] = "*" * len(sentence[i])
                break
    
    for word in sentence:
        print(word, sep= " ", end = " ")
    
if __name__ == "__main__":
    main()
