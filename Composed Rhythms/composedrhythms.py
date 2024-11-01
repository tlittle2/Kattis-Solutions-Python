def main():
    ip = int(input())
    
    l = []
    while ip >5: #6 (3*2) is as low as we can go before having to manually do cases
        l.append(3)
        ip-=3

    #is there a better way to do this?    
    if ip == 5:
        l.append(3)
        l.append(2)
    elif ip == 4:
        l.append(2)
        l.append(2)
    elif ip == 3:
        l.append(3)
    elif ip == 2:
        l.append(2)

    print(len(l))
    for i in l:
        print(i, sep = " ", end = " ")

if __name__ == "__main__":
    main()
