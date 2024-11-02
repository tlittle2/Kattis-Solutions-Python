def createKey(d, string):
    return ''.join([key for key,values in d.items() if string in values])

def main():
    lookup = {
        "c" : ["number of","fewest","fewer","many","few"],#count nouns
        "m" : ["amount of","least","less","much","little"], #mass nouns
        "cm": ["most", "more"] #count and mass nouns
    }

    words, phases = list(map(int, input().split()))

    #create nouns dictionary to have the same layout as the lookup dictionary
    nouns = dict()
    for _ in range(words):
        word,nounType = input().split()
        if nounType not in nouns:
            nouns[nounType] = [word]
        else:
            nouns[nounType].append(word)

    #if the prefix and the word having a matching key in the respective dictionaries, then it's a correct noun
    for _ in range(phases):
        line = input().split()
        prefix = ' '.join(line[0:len(line)-1]) 
        word = line[len(line)-1]
     
        prefixKey = createKey(lookup, prefix) #get the nounType for phrase prefix in lookup dictionary
        nounKey = createKey(nouns, word) #get the nounType for last word of phrase in noun dictionary
      
        print("Correct!" if nounKey in prefixKey else "Not on my watch!")

if __name__ == "__main__":
    main()
