def main():
    while True:
        x,y = map(int, input().split())
        
        if x == 0 and y == 0:
            break

        if x + y == 13:
            print("Never speak again.")
            continue

        if x > y:
            print("To the convention.")
        elif x < y:
            print("Left beehind.")
        else:
            print("Undecided.")
        

if __name__ == "__main__":
    main()
