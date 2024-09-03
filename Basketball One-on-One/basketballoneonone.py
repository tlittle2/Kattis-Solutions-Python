def main():
    aScore= 0
    bScore= 0

    ip = input()
    for i in range(len(ip)):
        if ip[i]== 'A':
            aScore+=int(ip[i+1])
            #print(aScore)
        elif ip[i] == 'B':
            bScore+=int(ip[i+1])
            #print(bScore)

    if aScore > bScore:
        print('A')
    else:
        print('B')
   
if __name__ == "__main__":
    main()
