def findDiffs(lst):
    differences = set()

    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        differences.add(diff)

    if len(differences) == 1:
        return True
    return False

def main():
    for _ in range(int(input())):
        lst = list(map(int, input().split()))
        lst.remove(lst[0])

        #These types of lists can only exist if the list sorted in some way (pre-sorted of sorted manually)
        if findDiffs(lst): # if the original list satisfies criteria (already sorted)
            print("arithmetic")
        elif findDiffs(sorted(lst)) or findDiffs(sorted(lst, reverse= True)): #if a manually sorted list satisfies criteria
            print("permuted arithmetic")
        else:
            print("non-arithmetic")    

if __name__ == "__main__":
    main()
