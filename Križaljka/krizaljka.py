#partially right

def getEarliest(a,b): #get earliest from both words where we have a matching character
    return next((i for i, ch  in enumerate(a) if ch in b),None)

def main():
    a,b = input().split()

    aIndex = getEarliest(a,b)
    bIndex = getEarliest(b,a)

    grid = [["." for _ in range(len(a))] for _ in range(len(b))]
    
    grid[bIndex] = list(a) #place first word at correct location (replacing all "."'s with the letters of the word)

    idx = 0
    for i in grid: #for each letter of the second word, place each letter vertically at the correct location where 2 words cross
        i[aIndex] = list(b)[idx]
        idx+=1
        
    for i in grid: #print the letters of the grid after the fact
        print("".join(i))


if __name__ == "__main__": 
    main()
