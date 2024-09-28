def main():
    d = {
    'A' : [11,11],
    'K' : [4,4],
    'Q' : [3,3],
    'J' : [20,2],
    'T' : [10,10],
    '9' : [14,0],
    '8' : [0,0],
    '7' : [0,0]
    }
    

    cases, suit = input().split()

    s = 0
    for _ in range(4*int(cases)):
        ip = list(input())
        if ip[1] == suit:
            s += d[ip[0]][0]
        else:
            s += d[ip[0]][1]
    
    print(s)

if __name__ == "__main__":
    main()
