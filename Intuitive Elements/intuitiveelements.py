def main():
    for _ in range(int(input())):
        element = set(input())
        abbrev = set(input())
        print("YES" if len(element.intersection(abbrev)) == len(set(abbrev)) else "NO")
        
if __name__ == "__main__": 
    main()
