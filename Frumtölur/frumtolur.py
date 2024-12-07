def isPrime(n):
    if n == 0 or n == 1:
        return
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return 
    return n

def main():
    primes = list(filter(lambda x: x is not None, [isPrime(i) for i in range(2, 101)]))

    for i in range(5):
        print(primes[i])
      
if __name__ == "__main__":
    main()
