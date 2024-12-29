def main():
    lst = [-1,3,4,5,2,2,2,2]

    dp = [1 for _ in range(len(lst))] #acts as a sort of lookup table

    j = 1 #forward pointer
    while(j<len(lst)):
        i=0
        while(i != j): #until pointer i reaches pointer j
            if lst[j] >= lst[i]:
                dp[j]=max(dp[i], dp[j])+1 #this is the dp aspect. add to index in dp if 2 values satisfy comparison condition
            i+=1
        j+=1 #always advance j until we reach the end of the list

    print(max(dp))    

if __name__ == "__main__":
    main()
