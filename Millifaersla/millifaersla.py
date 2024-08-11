def main():
    l = list()

    for _ in range(3):
        l.append(int(input()))
    
    match l.index((min(l))):
        case 0:
            print("Monnei")
        case 1:
            print("Fjee")
        case 2:
            print("Dolladollabilljoll")

if __name__ == "__main__":
    main()
