#!/usr/bin/env python3


def main():

    n = int(input())


    for i in range(n):
        sYB = True
        bYB = True
        cB = True
        
        s = input().split()

        name = s[0]
        studies = s[1]
        birth = s[2]
        courses = int(s[3])

        
        sYear = int(studies[0:4])
        bYear = int(birth[0:4])
        if sYear < 2010:
            sYB = False
        
        if bYear < 1991:
            bYB=False

        if not sYB and not bYB:
            if courses <= 40:
                cB = False


        if not sYB and not bYB and not cB:
            print("{} coach petitions".format(name))
        elif not sYB and not bYB and cB:
            print("{} ineligible".format(name))
        else:
            print("{} eligible".format(name))


if __name__ == "__main__":
    main()