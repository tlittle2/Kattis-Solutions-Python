#/usr/bin/env python3
import sys

def main():
    rows,cols,rack= [int(x) for x in sys.stdin.readline().split()]
    window=[]
    for i in range(rows):
        print(window.append(list(sys.stdin.readline().rstrip())))
        count= 0

    for i in range(rows-rack+1):
        for j in range(cols-rack+1):
            for k in range(i+1, i+rack-1):
                count+=window[k][j+1: j+rack-1].count('*')
    print(count)
    for i in range(rows):
        print(''.join(window[i]))

if __name__ == "__main__":
    main()