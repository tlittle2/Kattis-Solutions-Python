#/usr/bin/env python3

import sys

def main():
    while True:
        hour, minute= map(int, sys.stdin.readline().split())


        newMinute= minute - 45


        if newMinute < 0:
            hour-=1
            
        print(hour%24, newMinute%60)

if __name__ == "__main__":
    main()