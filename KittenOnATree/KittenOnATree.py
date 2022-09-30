#/usr/bin/env python3
#Trevor Little


kitten= int(input())
branchlist= []
b= [0]

print(kitten, end= ' ')


while True:
    b = [int(x) for x in input().split()]
    if b[0] == -1:
        break
    branchlist.append(b)

kittenFound= False

for x in range(100):
    for i in branchlist:
        for j in range(1, len(i)):
            if i[j]== kitten:
                print(i[0], end= ' ')
                kitten= i[0]
                kittenFound= True
                break
        if kittenFound==True:
            kittenFound= False
            break