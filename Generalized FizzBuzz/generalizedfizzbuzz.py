def main():
    n,a,b = map(int, input().split())

    f = "fizz"
    bz = "buzz"
    fb = "fizzbuzz"
    
    d = {
        f: 0,
        bz: 0,
        fb: 0
    }

    for i in range(1, n+1):
        if i % a == 0 and i % b ==0:
            d[fb]+=1
        elif i % a == 0:
            d[f]+=1
        elif i % b == 0:
            d[bz]+=1

    print("{} {} {}".format(d[f],d[bz],d[fb]))
    

if __name__ == "__main__":
    main()
