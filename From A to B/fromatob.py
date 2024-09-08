def main():
    a,b = map(int, input().split())
    moves = 0

    while a!=b:
        if a < b: #if a is less than b, we must increase our moves and our 'a' by the range between b-a
            moves+=b-a
            a+=b-a
        elif a % 2!=0:
            moves+=1
            a+=1
        else:
            moves+=1
            a = int(a/2)

    print(moves)
if __name__ == "__main__":
    main()
