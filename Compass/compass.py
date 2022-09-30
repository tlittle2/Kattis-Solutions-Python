#/usr/bin/env python3

def main():
    curr = int(input())
    dest = int(input())

    right = (dest - curr) % 360
    left = (curr-dest) % 360


    if left < right:
        print(-(left))
    else:
        print(right)

if __name__ == "__main__":
    main()