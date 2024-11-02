def main():
    countNoun = "c"
    massNoun = "m"
    both = "cm"

    lookup = {
        countNoun : ["number of","fewest","fewer","many","few"],
        massNoun : ["amount of","least","less","much","little"],
        both: ["most", "more"]
    }

    words, phases = list(map(int, input().split()))

    nouns = dict()
    for _ in range(words):
        word,type = input().split()
        if type not in nouns:
            nouns[type] = [word]
        else:
            nouns[type].append(word)

  
    for _ in range(phases):
        line = input().split()
        
        if len(line) > 2: #if length of line is 2, it means the line contains one of the longer keys (and we have to account for this accordingly)
            prefix = ' '.join(line[0:len(line)-1]) 
            word = line[len(line)-1]
        else:
            prefix = line[0]
            word = line[1]

      
        nounKey = ''.join([k for k,v in nouns.items() if word in v])
        prefixKey = ''.join(([k for k,v in lookup.items() if prefix in v]))

        print("Correct!" if nounKey in prefixKey else "Not on my watch!")

if __name__ == "__main__":
    main()
