def main(): 
    s = list(input())
    new=[]
    count= 0

    for i in range(len(s)-1, -1, -1):
        if s[i] == '<':
            new.append(" ")
            count+=1
        elif count > 0:
            new.append(" ")
            count-=1
        else:
            new.append(s[i])

    print(''.join([i for i in list(reversed(new)) if i != " "]))
if __name__ == "__main__":
    main()
