def addToMap(m, k):
    m[k] +=1

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
            addToMap(d,fb)
        elif i % a == 0:
            addToMap(d,f)
        elif i % b == 0:
            addToMap(d,bz)
            
    print("{} {} {}".format(d[f],d[bz],d[fb]))
    

if __name__ == "__main__":
    main()
