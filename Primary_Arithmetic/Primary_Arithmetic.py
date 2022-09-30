#/usr/bin/env python3

def main():
    for i in range(50):
        num1, num2= input().split()
        
        if int(num1) == 0 and int(num2) == 0:
            break
        num1=num1.zfill(10)
        num2=num2.zfill(10)
        
        
        num1= num1[::-1]
        num2= num2[::-1]
        
        numOfCarries = 0
        carry = 0
        for j in range(10):
            if int(num1[j]) + int(num2[j]) + carry > 9:
                numOfCarries += 1
                carry = 1
            else:
                carry = 0

        if numOfCarries == 0:
                    print("No carry operation.")
        if numOfCarries == 1:
                    print("1 carry operation.")
        if numOfCarries > 1:
                    print(numOfCarries, "carry operations.")

if __name__ == "__main__":
    main()