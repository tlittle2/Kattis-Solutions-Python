def main():
    _, window = map(int, input().split())
    lst = list(map(int, input().split()))

    if window > len(lst) or window <= 0: #edge case for 0 or window > size of list
        print(0)
        return
    
    count = 0
    for i in range(len(lst) - window+1): #loop up to len(lst) - window + 1 to avoid index-out-of-bounds
        w = lst[i:i+window]
        if len(list(filter(lambda x: x % 2 == 0, w))) >=2: #if the number of even numbers in this subarray >=2, add to the count
            count += 1
    print(count)

if __name__ == "__main__":
    main()
