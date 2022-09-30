#!/usr/bin/env python3

import math
import sys

def main():
    i = 1
    for l in sys.stdin:
        vals = [int(i) for i in l.split()]
        print("Case {}: {} {} {}".format(i, min(vals[1::]), max(vals[1::]), max(vals[1::]) - min(vals[1::])))

        i+=1







if __name__ == "__main__":
    main()