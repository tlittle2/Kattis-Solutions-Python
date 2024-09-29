#got time limited exceeded, but is accepted

def main():
    ip = input()
    l = list(map(int,ip))
    num = int(ip)
    
    s = sum(l)

    comp = str(num + 1)
    
    while sum(list(map(int,comp))) != s:
        comp = str(int(comp)+1)
    
    print(comp)   
            
if __name__ == "__main__": 
    main()
