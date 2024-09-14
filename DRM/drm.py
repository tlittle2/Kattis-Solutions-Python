from string import ascii_uppercase as up

def rotate(lst):
    sum = 0
    for i in lst:
        sum+=up.index(i)    

    for i in range(len(lst)):
        idx = (up.index(lst[i])+ sum) % len(up)
        lst[i] = up[idx]

    return lst

def main():
    drm = input()

    split= len(drm) // 2

    #divide
    lst1= [drm[i] for i in range(0,split)]
    lst2= [drm[i] for i in range(split,len(drm))]

    #rotate
    newlst1 = rotate(lst1)
    newlst2 = rotate(lst2)

    #merge
    #print("".join(up[(up.index(newlst1[i]) + up.index(newlst2[i])) % len(up)] for i in range(len(newlst1))))
    s = ""
    for i in range(len(newlst1)):
        #s+=up[(up.index(newlst1[i]) + up.index(newlst2[i])) % len(up)]
        new = up.index(newlst1[i]) + up.index(newlst2[i])
        s+=up[new % len(up)]

    print(s)

if __name__ == "__main__":
    main()
