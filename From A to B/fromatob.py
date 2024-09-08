"""
time limit exceeded
"""

def main():
    a,b = map(int, input().split())

    moves = 0
    while a!=b:
        if a <b:
            a+=1
            moves+=1
        
        elif a % 2!=0:
            a+=1
            moves+=1
        else:
            a = int(a/2)
            moves+=1
    print(moves)
                


if __name__ == "__main__":
    main()
