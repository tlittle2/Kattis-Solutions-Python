#partially right

def getEarliest(a,b): #get earliest from both words where we have a matching character
    return next((i for i, ch  in enumerate(a) if ch in b),None)

def main():
    a,b = map(list,input().split())

    aIndex = getEarliest(a,b)
    bIndex = getEarliest(b,a)

    grid = [["." for _ in range(len(a))] for _ in range(len(b))]
    
    grid[bIndex] = a

    for i in range(len(b)):
        grid[i][aIndex] = b[i]
            
    for i in grid:
        print("".join(i))

if __name__ == "__main__": 
    main()
