def main():
    binaries = {
    '0': '....',
    '1': '...*',
    '2': '..*.',
    '3': '..**',
    '4': '.*..',
    '5': '.*.*',
    '6': '.**.',
    '7': '.***',
    '8': '*...',
    '9': '*..*'
    }

    lst = [binaries[i] for i in input()] #get all of the correct binary values and store them into a list (each value will have its own indice)

    tLst = [list(i) for i in zip(*lst)] #transpose original list and make a list of list out of it
    
    for t in tLst:
        t.insert(2, " ") #add required space in the middle of each input (index 2)

    for t in tLst:
        print(" ".join(t)) #print the output in the desired format

if __name__ == "__main__":
    main()
