#!/usr/bin/env python3

def main():
    n, x = map(int, input().split())

    #if we have item or fewer, our answer is going to be 1 because we are always accounting at least one item
    if n < 2:
        print(1)
        return 

    lst = []
    for i in input().split():
        lst.append(int(i))

    #we want to mark as many items as possible. To do this, we want to sort the list so no one gets suscipious
    lst = sorted(lst)
    
    #we will always account for the first value no matter what
    ans = 1


    #as we go through the sorted list, if the current number and the number before are less than x, we will allocate to our total
    #Once we go over, we break out of the loop and we tell them how many items we accounted
    for i in range(1, len(lst)):
        if lst[i] + lst[i-1] <= x:
            ans+=1
        else:
            break


    print(ans)





if __name__ == "__main__":
    main()