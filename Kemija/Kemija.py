#/usr/bin/env python3
import sys


def main():
    s= str(sys.stdin.readline().strip())

    s= s.replace('apa', 'a')
    s= s.replace("epe","e");
    s= s.replace("ipi", "i");
    s= s.replace("opo", "o");
    s= s.replace("upu", "u");

    print(s)

if __name__ == "__main__":
    main()