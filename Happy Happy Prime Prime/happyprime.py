def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False 
    return True

def isHappy(n):
    if int(n) == 1: #as per the problem, 1 should not be considered a prime
        return False
        
    ans = 0
    for i in list(str(n)):
        ans+= int(i) ** 2
        
    if(len(str(ans)) == 1): #continue recursing until the length of the string is 1
        if int(ans)==7: #The only single digit number that ALWAYS works is 7
            return True
        elif int(ans) == 1: #if the answer is 1, then it's happy
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
