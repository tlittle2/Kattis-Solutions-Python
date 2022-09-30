#/usr/bin/env python3

def main():

    lower = 1
    higher = 1000

    while True:
        mid = lower + higher // 2
        x = input()
        if x == "higher":
            higher = mid + 1
        if x == "lower":
            lower = mid -1

        if x == "correct":
            break


if __name__ == "__main__":
    main()