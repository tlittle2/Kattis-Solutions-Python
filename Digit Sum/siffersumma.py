def main():
    ip = input()
    s = sum(list(map(int,ip)))
    
    comp = str(int(ip) + 1)

    while sum(list(map(int,comp))) != s:
        comp = str(int(comp)+1)
    
    print(comp)
            
if __name__ == "__main__": 
    main()
