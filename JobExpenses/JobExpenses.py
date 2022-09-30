#/usr/bin/env python3
import sys

def main():
    num= int(sys.stdin.readline())
    total = 0
    values= []

    for i in sys.stdin.readline().split():
        values.append(i)

    for i in range(len(values)):
        #print(values[i])
        if int(values[i]) < 0:
            total += int(values[i])

    print(total - total - total)

if __name__ == "__main__":
    main()