def main():
    syllables, numOfPlayers= map(int, input().split())

    hands = []

    for i in range(numOfPlayers):
        hands.append([i+1,3])

    #print(hands)

    index= 0
    while(True):
        if len(hands) == 1:
            print(hands[0][0])
            break

        index+=syllables - 1
        index= index % len(hands)

        if (hands[index][1] == 3):
            tempPlayer= hands[index][0]
            hands.pop(index)
            hands.insert(index, [tempPlayer,2])
            hands.insert(index, [tempPlayer,2])
        elif (hands[index][1] == 2):
            hands[index][1]=1
            index+=1
        else:
            hands.pop(index)
    
if __name__ == "__main__":
    main()
