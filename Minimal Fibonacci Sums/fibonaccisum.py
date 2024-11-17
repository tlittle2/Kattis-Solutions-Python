def generateFib(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    
    while fib_list[-1] + fib_list[-2] <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list

def main():
    num = int(input())
    fibList = sorted(generateFib(num),reverse=True) #generate reverse sorted list of all fibonacci numbers up to n

    valsToConsider = list(filter(lambda x: x<=num, fibList)) # we only care about numbers up to input number

    vals = [valsToConsider[0]] #first value of our answer should be biggest fibonacci number we can get without going over

    for i in valsToConsider[1:]:
            if sum(vals) + i <= num: #check if we go over our input number if we add this number to our current sum
                vals.append(i)
    
    print(" ".join(list(str(i) for i in sorted(vals)[1:])))

if __name__ == "__main__":
    main()
