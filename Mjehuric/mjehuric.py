#Literally bubble sort
def main():
    arr = list(input().split())

    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(' '.join(arr))
    
if __name__ == "__main__": 
    main()
