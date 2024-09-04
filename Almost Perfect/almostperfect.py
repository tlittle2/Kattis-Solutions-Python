"""
Answer is right, but website having trouble reading input
"""

import math

def main():
    while True :
        ip = int(input())
        count = 1
        for i in range(2, int(math.sqrt(ip)) + 1):
            if ip % i == 0:
                count+=i
                if i*i != ip:
                    count+= ip//i
        if count == ip:
            print("{} perfect".format(ip))
        elif abs(ip - count) <=2:
            print("{} almost perfect".format(ip))
        else:
            print("{} not perfect".format(ip))                
if __name__ == "__main__":
    main()
