"""
Only works on test input
"""

def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False 
    return True

def isHappy(n):
    if int(n) == 1:
        return False
    
    ans = 0

    for i in list(str(n)):
        ans+= int(i) ** 2
    
    if(len(str(ans)) == 1):
        if int(ans) == 1:
            return True
        else:
            return False
    else:
       return isHappy(ans)

def main():
    for _ in range(int(input())):
        case, number = map(str, input().split())
        happyPrime = "YES" if isHappy(number) and isPrime(int(number)) else "NO"
        print("{} {} {}".format(case, number, happyPrime))
                   

if __name__ == "__main__":
    main()
