#!/usr/bin/env python3

import sys


dict = {}

def calc(string):
    operations= string.split()[1::2]
    listOfValues = []
    none= False
    words = string.split()[::2]
    ans = 0
    newString = ""

    for i in words:
        listOfValues.append(dict.get(i))

    for i in range(len(words)):
        newString+= str(listOfValues[i]) + " "
        newString+= operations[i] + " "
    
    #print(newString)
    
    if newString.count("None") > 0:
        none = True
        return "{0}unknown".format(string)
    else:
        ans = eval(newString[0:len(newString)-2:1])
        for key, value in dict.items():
            if ans == int(value):
                return "{0}{1}".format(string, key)

        return "{0}unknown".format(string)


def define(param1, param2):
    param2 = param2
    dict[param1] = param2
    #print(dict)
    pass

def main():
    #read input
    for i in sys.stdin:
        o = i.split()
        if o[0] == "def":
            define(o[1], o[2])
        
        elif o[0] == "calc":
            s = ""
            for i in range(1, len(o)):
                s += o[i] + " "
            print(calc(s))
        else:
            dict.clear()


if __name__ == "__main__":
    main()