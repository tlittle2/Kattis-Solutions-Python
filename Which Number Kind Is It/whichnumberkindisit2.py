import math

def isSquare(n):
    return "S" if math.sqrt(n).is_integer() else ""

def isOdd(n):
    return "O" if  n % 2 == 1 else ""

def main():
    for _ in range(int(input())):
        num = int(input())
        s = "{}{}".format(isOdd(num), isSquare(num))
        print("EMPTY" if not s else s)
        
if __name__ == "__main__":
    main()
