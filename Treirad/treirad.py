def main():
    v = int(input())
    
    start = 1
    c = 0

    while start * (start + 1) * (start +2) < v:
            c+=1
            start+=1

    print(c)


if __name__ == "__main__":
    main() 
