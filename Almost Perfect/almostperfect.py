import math
import sys

def main():
    for line in sys.stdin:
        ip = int(line)
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
