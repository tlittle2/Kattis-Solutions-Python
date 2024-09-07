def main():
    lst = [0,0,0]

    for _ in range(int(input())):
        ip = input().split()
        if ip[0] == 'J':
            lst[0]+=1
        if ip[1] == 'J':
            lst[1]+=1
        if ip[2] == 'J':
            lst[2]+=1
            
    print(min(lst))

if __name__ == "__main__":
    main()
