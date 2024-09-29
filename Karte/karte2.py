def main():
    suits = ['P', 'K', 'H', 'T']
    d = {}

    ip = input()

    #append cards to dictionary
    for i in range(0,len(ip), 3):
        if ip[i] not in d.keys():
            d[ip[i]] = [ip[i+1:i+3]]
        else:
            d[ip[i]] += [ip[i+1:i+3]]

    #any missing cards get a value of 0. As per the problem, we cannot ever have 0 as a value for a card
    noCardValue = 0
    for i in suits:
        if i not in d.keys():
            d[i] = [noCardValue]


    #calculate answer
    lst = []
    cardsPerSuit = 13
    greska = "GRESKA"
    for i in suits:
        if (len(set(d[i])) < len(d[i])): #compare the actual list to the list as a set (to remove duplicates and compare counts)
            lst.append(greska)
        elif noCardValue in d[i]: #If 0 is the value for this suit, it will automatically be 13
            lst.append(cardsPerSuit)
        else:
            lst.append(cardsPerSuit - len(d[i]))
    
    if greska in lst:
        print(greska)
    else:
        for i in lst:
            ' '.join([i for i in lst])

if __name__ == "__main__":
    main()
