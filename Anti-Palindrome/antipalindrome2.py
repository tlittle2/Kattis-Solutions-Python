from string import ascii_letters

def isPalindrome(s):
    return s == s[::-1]

def main():
    ip = (list((i.lower()) for i in input() if i in ascii_letters))
    found = False
    
    for i in range(len(ip)):
        if found:
            break
        for j in range(i+2, len(ip)+1):
            #print("{} {} {}".format(i,j,ip[i:j]))
            if isPalindrome(ip[i:j]):
                found = True
                break

    if found:
        print("Palindrome")
    else:
        print("Anti-palindrome")
                        
if __name__ == "__main__":
    main()
