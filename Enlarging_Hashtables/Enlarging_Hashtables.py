#/usr/bin/env python3
def prime(y):
    if y==2:
        return True
    if y & 1 == 0:
        return False
    d=3
    while d * d <= y:
        if y % d == 0:
            return False
        d= d+2
    return True

n= int(input())
while n!=0:
    twon= (n * 2) + 1
    i= 0
    while i < 2**30:
        f= (twon)+(2*i)
        if prime(f):
            break
        else:
            i+=1
    if prime(n):
         print(f)            
    else:
        print(f, " (", n, " is not prime)",sep= '')
           
    n=int(input())