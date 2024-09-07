def main():
    ip = [int(i) for i in list(input())] #make each digit of stdin input into its own indice in a list
    mstr = [i for i in range(1, len(ip)+1)] #make custom list of values from 1 until the last value in the list created from stdin

    print(ip[len(ip)-1] if ip == mstr else -1) #if the lists are the exact same, print the last int in the list created from stdin
    
if __name__ == "__main__":
    main()
