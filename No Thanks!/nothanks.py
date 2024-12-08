def main():
    int(input())
    l = sorted(list(map(int, input().split())))
    s = set()

    r = 1
    i = 0

    while i < len(l):
        temp = l[i]
        j = i+1 #at the start, j will always be 1 index after where are currently at
        while j < len(l) and abs(l[j]-l[i]) == r:
            temp = min(temp, l[j])
            r+=1
            j+=1
        s.add(temp)
        i=j #start i from where consecutive numbers stopped
        r=1 #reset the range back to 1 after consecutive numbers stopped
    print(sum(s))
        
if __name__ == "__main__": 
    main()
