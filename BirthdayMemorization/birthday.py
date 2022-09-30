#!/usr/bin/env python3


def main():
    l = list()
    n = int(input())

    for i in range(n):
        tempList= []
        name, num, birth = input().split()
        num = int(num)
        tempList.append(name)
        tempList.append(num)
        tempList.append(birth)
        l.append(tempList)
    
    l = sorted(l, key = lambda x: x[1], reverse= True)


    print()
    print(l)

    
    for i in range(len(l)):
        print(i)
        curr = l[i][2]
        #print("CURR ------> {}".format(curr))
        for j in range (len(l)-1):
            if i == j:
                continue
            #print(len(l))
            print("{} {}".format(i, j))
            compare = l[j][2]
            #print("     COMPARE ------> {}".format(compare))
            if curr == compare:
                print("SAME DATE")
                #print("{} {}".format(l[i], l[j]))
                if l[i][1] > l[j][1]:
                    l.remove(l[j])
                else:
                    l.remove(l[i])
        
            print("NEW LIST: {}".format(l))
    
    
    print(len(l))
    for i in l:
        print(i[0])


if __name__ == "__main__":
    main()