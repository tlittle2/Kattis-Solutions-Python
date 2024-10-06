def main():
    names, initials = map(int, input().split())

    d = {}

    for _ in range(names):
        ip = input()
        # create copy of input to get initials for dictionary
        cp = ip.split()
        cpInitials = "{}{}".format(cp[0][0],cp[1][0])

        #if the initials are not in the dictionary, create a new entry for those initials as a list. Otherwise, append to the already existing list
        if cpInitials not in d:
            d[cpInitials] = [ip]
        else:
            d[cpInitials].append(ip)

    initialList = []

    for _ in range(initials):
        initialList.append(input())
    
    #create output
    for i in initialList:
        if i in d.keys():
            if len(d[i]) == 1:
                print(''.join(d[i]))
            else:
                print("ambiguous")
        else:
            print("nobody")

if __name__ == "__main__":
    main()
