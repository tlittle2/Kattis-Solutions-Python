def main():
    ip = input()
    s = sum(list(map(int,ip)))
    num = int(ip)
    
    comp = str(num + 1)

    while sum(list(map(int,comp))) != s:
        comp = str(int(comp)+1)
    
    print(comp)
            
if __name__ == "__main__": 
    main()
