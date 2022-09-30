#!/usr/bin/env python3

import sys

def naive(p, word):
    indices = []
    for i in range(len(word)):
        #if find our pattern, we append it to the indice list
        if word[i:i+len(p)] == p[0:len(p)]:
            indices.append(i)
        else:        
            i = i+len(p)
            

    for i in indices:
        print("{} ".format(i),end = "")
            
    print()



def KMP(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
  
    initial_point = []
    m = 0
    n = 0
  
    while m != a:
       
        if text[m] == pattern[n]:
            m += 1
            n += 1
      
        else:
            n = prefix_arr[n-1]
       
        if n == b:
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1
   
    return initial_point

def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
                n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr



def main():
    for line in sys.stdin:
        p = [i for i in line.rstrip('\n')]
        if len(p) == 0:
            break
        else:
            word = [i for i in input()]

        #print(p)
        #print(word)

        for i in KMP(p,word):
            print("{} ".format(i),end = "")


            


    




if __name__ == "__main__":
    main()