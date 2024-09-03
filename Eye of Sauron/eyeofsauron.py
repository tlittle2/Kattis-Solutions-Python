def main():
    ip= input()

    lst = list()

    for i in ip:
        lst.append(i)

    aIndice = 0
    bIndice = 0

    #preprocess the list to find our indicies
    for i in range(len(lst)):
        if lst[i] == '(':
            aIndice = i
            bIndice = i+1

    #if certain counts are not the same, it needs to be 'fixed'
    if aIndice != (len(lst)-1)- bIndice:
        print("fix")
    else:
        print("correct")
    
if __name__ == "__main__":
    main()
