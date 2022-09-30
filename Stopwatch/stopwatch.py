#!/usr/bin/env python3



def main():
    n = int(input())

    running = True

    lastTime = int(input())

    total = 0


    for i in range(n-1):
        ip = int(input())

        if not running:
            running = True
            lastTime = ip

        else:
            running = False
            total+=ip - lastTime

    if running:
        print("still running")
    else:
        print(total)


if __name__ == "__main__":
    main()