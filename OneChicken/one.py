#!/usr/bin/env python3


def main():
    n,m = input().split()

    n = int(n)
    m = int(m)
    
    if n < m:
        if m -n == 1:
            print("Dr. Chaz will have {} piece of chicken left over!".format(m-n))
        else:
            print("Dr. Chaz will have {} pieces of chicken left over!".format(m-n))

    else:
        if n - m == 1:
            print("Dr. Chaz needs {} more piece of chicken!".format(n-m))
        else:
            print("Dr. Chaz needs {} more pieces of chicken!".format(n-m))




if __name__ == "__main__":
    main()