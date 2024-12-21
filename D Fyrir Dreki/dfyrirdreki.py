def main():
    a = int(input())
    b = int(input())
    c = int(input())

    d = (b ** 2) - (4*a*c)
    
    if d > 0:
        print(2)
    elif d == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__": 
    main()
