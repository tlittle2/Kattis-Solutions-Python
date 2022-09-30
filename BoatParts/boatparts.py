#!/usr/bin/env python3

s= set()

def main():
    p, n = map(int, input().split())

    days = 0
    for i in range(n):
        part = input()
        s.add(part)
        if len(s) == p:
            print(i+1)
            break
    
    else:
        print("paradox avoided")

if __name__ == "__main__":
    main()