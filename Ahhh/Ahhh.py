#/usr/bin/env python3

import sys

def main():
    mAhh= str(sys.stdin.readline())

    dAhh= str(sys.stdin.readline())


    if(len(mAhh) >= len(dAhh)):
        print('go')
    else:
        print('no')

if __name__ == "__main__":
    main()