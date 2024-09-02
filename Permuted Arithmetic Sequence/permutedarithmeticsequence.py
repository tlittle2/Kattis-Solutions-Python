def findDiffs(lst): #find the distinct differences between the current element and the next element
    differences = set()

    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        differences.add(diff)
    #if the length is 1, then we have our arithmetic sequence
    if len(differences) == 1:
        return True
    return False

def main():
    for _ in range(int(input())):
        lst = list(map(int, input().split()))
        lst.remove(lst[0])
      #these types of lists can ONLY happen if the list is sorted
        s = sorted(lst)
        r = sorted(lst, reverse= True)
        
        lstDiff = findDiffs(lst)
        sDiff = findDiffs(s)
        rDiff = findDiffs(r)
      
        if lstDiff: #if the original list satisfied the criteria
            print("arithmetic")
        elif sDiff or rDiff: #if we had to sort the original list to satisfy the criteria
            print("permuted arithmetic")
        else:
            print("non-arithmetic")    

if __name__ == "__main__":
    main()
