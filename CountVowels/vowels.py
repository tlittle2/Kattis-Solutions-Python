#/usr/bin/env python3


def main():
    vowels = set('aeiouAEIOU')
    
    s = list(input())

    num = 0 
    
    for i in s:
        if i in vowels:
            num+=1

    print(num)

    
if __name__ == "__main__":
    main()