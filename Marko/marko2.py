#gets time limited exceeded because we have to loop through lists
def main():
    phone = {
    1 : [" "],
    2 : ['a','b','c'],
    3 : ['d','e','f'],
    4 : ['g','h','i'],
    5 : ['j','k','l'],
    6 : ['m','n','o'],
    7 : ['p','q','r','s'],
    8 : ['t','u','v'],
    9 : ['w','x','y','z']
    }

    mp = {}

    for _ in range(int(input())):
        word = input()
        cnvrt = ""
        for c in word:
            for k,v in phone.items():
                if c in v:
                    cnvrt += str(k)
            mp[word] = int(cnvrt)

    comp = int(input())

    print(len([v for v in mp.values() if v == comp]))  
    

if __name__ == "__main__":
    main()
