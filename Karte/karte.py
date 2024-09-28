def main():
    suits = ['P', 'K', 'H', 'T']
    d = {}

    ip = input()

    #append cards to dictionary
    for i in range(0,len(ip), 3):
        if ip[i] not in d.keys():
            d[ip[i]] = [int(ip[i+1:i+3])]
        else:
            d[ip[i]] += [int(ip[i+1:i+3])]

    #any missing cards get a value of 0. As per the problem, we cannot ever have 0 as a value for a card
    noCardValue = 0
    for i in suits:
        if i not in d.keys():
            d[i] = [noCardValue]


    #calculate answer
    st = ""
    cardsPerSuit = 13
    for i in suits:
        if (len(set(d[i])) < len(d[i])): #compare the actual list to a set of the list (to remove duplicates and compare counts)
            st = "GRESKA" #final string will automatically be GRESKA if we find ANY cases where we have duplicate cards
            break
        else:
            if noCardValue in d[i]: #. If 0 is the value for this suit, it will automatically be 13
                st+="{} ".format(cardsPerSuit)
            else:
                st+="{} ".format(cardsPerSuit - len(d[i]))
    
    print(st)

if __name__ == "__main__":
    main()
