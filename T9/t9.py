#!/usr/bin/env python3


import sys


dict = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    " ": '0'


    }

def main():
    l = list()
    x = int(input())

    for i in range(x):
        result = ""
        word = str(input())
        for j in range(len(word)):
            l.append(dict.get(word[j]))
        
        result+= l[0]
        for j in range(0, len(l)-1):
            if l[j] == l[j+1]:
                #print("These values are the same {0} {1}".format(l[i], l[i+1]))
                result+= " " + l[j+1]

            elif l[j][0] == l[j+1][0]:
                #print("These values use the same button {0} {1}".format(l[i], l[i+1]))
                result+= " " +l[j+1]
            
            else:
                #print("in else case {0} {1}".format(l[i], l[i+1]))
                result+=l[j+1]
        print("Case #{0}: {1}".format(i+1,result))
        l.clear()


if __name__ == "__main__":
    main()