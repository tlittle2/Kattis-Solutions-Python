#!/bin/usr/env python3



def main():
    first = [c for c in input()]
    second = [c for c in input()]
    c = 0

    for i in range(4):
        if first[i] != second[i]:
            c+=1
    
    print(2 ** c)



if __name__ == "__main__":
    main()