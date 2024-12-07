def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return True

def main():
    primes = [i for i in range(2, 10000) if isPrime(i)]
    
    for i in range(100):
        print(primes[i])


if __name__ == "__main__":
    main()
