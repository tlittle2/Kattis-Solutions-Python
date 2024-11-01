def transformedNumber(num):
    d = {2:5, 5:2}
    
    #answer is the original number backwards, and replace the key with the value from the dictionary
    newNumList = [d.get(k, k) for k in num[::-1]] 
    return int(''.join(map(str, newNumList)))
   
def main():
    x, y = map(lambda s: list(map(int, s)), input().split())
    print(1 if transformedNumber(x) > transformedNumber(y) else 2)

if __name__ == "__main__":
    main()
