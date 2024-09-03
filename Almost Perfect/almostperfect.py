"""
Note, doesn't work on larger inputs
"""
def get_divisors(n):
    l = list()
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            l.append(i)
    return l

def main():
    while True :
        ip = int(input())
        l = get_divisors(ip)
        s = sum(i for i in l)
        if s == ip:
            print("{} perfect".format(ip))
        
        elif (ip - s) <=2:
            print("{} almost perfect".format(ip))
        
        else:
            print("{} not perfect".format(ip))
    
if __name__ == "__main__":
    main()
