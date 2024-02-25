def main():
    l = list()

    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))


    idx = l.index(min(l))

    if idx == 0:
        print("Monnei")
    elif idx == 1:
        print("Fjee")
    elif idx ==2:
        print("Dolladollabilljoll")
        

if __name__ == "__main__":
    main()
