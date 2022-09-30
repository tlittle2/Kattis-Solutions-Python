#!/usr/bin/env python3

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

    #divide
    lst1= []
    lst2= []

    split= len(drm) // 2

    for i in range(0, split):
        lst1.append(drm[i])

    for i in range(split, len(drm)):
        lst2.append(drm[i])

    #rotate
    newlst1 = rotate(lst1)
    newlst2 = rotate(lst2)


    #merge
    s = ""
    for i in range(len(newlst1)):
        new = up.index(newlst1[i]) + up.index(newlst2[i])
        s+=up[new % 26]

    print(s)



if __name__ == "__main__":
    main()
