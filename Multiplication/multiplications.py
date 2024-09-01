from functools import reduce

def main():    
    n = int(input())
    l = [int(input()) for _ in range(n)]

    print(reduce((lambda x, y: x * y), l) % (10**9 + 7))

if __name__ == "__main__":
    main()
