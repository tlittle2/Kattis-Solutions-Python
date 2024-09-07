def main():
    lst = {'A', 'E', 'I', 'O', 'U'}
    ip = input()
    print( "Jebb" if lst.intersection(ip) else "Kannski" if ip == 'Y' else "Neibb")
if __name__ == "__main__":
    main()
