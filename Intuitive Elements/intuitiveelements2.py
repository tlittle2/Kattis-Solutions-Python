def main():
    for _ in range(int(input())):
        element = input()
        abbrev = input()

        b = True
        for letter in abbrev:
            if letter not in element:
                b = False
                break
        print("YES" if b else "NO")
        
if __name__ == "__main__": 
    main()
