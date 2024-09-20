def populateMap(n):
    d = {}
    for _ in range(n):
        ans = input()
        if ans not in d.keys():
            d[ans] = 1
        else:
            d[ans]+= 1
    return d

def updateMap(d1, d2):
    for k in d2.keys():
        if k not in d1.keys():
            d1[k] = 0
    return d1

def main():
    n = int(input())
    #append inputs to respective dictionaries
    first = populateMap(n)
    second = populateMap(n) 
    
    #make sure map1 and map2 have each others keys
    first = updateMap(first, second)
    second = updateMap(second,first)

    #the answer is the sum of the minimum value for each key from both of dictionaries (both dictionaries have the same keys, so the dictionary we choose to iterate through does not matter)
    print(sum(min(first[k], second[k]) for k in first.keys()))

if __name__ == "__main__":
    main()
