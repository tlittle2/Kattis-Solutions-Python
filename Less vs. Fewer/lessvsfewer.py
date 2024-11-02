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
        word,type = input().split()
        if type not in nouns:
            nouns[type] = [word]
        else:
            nouns[type].append(word)

    #if the prefix and the word having a matching key in the respective dictionaries, then it's a correct noun
    for _ in range(phases):
        line = input().split()
        prefix = ' '.join(line[0:len(line)-1]) 
        word = line[len(line)-1]
     
        nounKey = ''.join([k for k,v in nouns.items() if word in v])
        prefixKey = ''.join(([k for k,v in lookup.items() if prefix in v]))

        print("Correct!" if nounKey in prefixKey else "Not on my watch!")

if __name__ == "__main__":
    main()
