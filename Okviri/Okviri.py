#/usr/bin/env python3

def main():
    word= str(input())

    #first line
    print('.', end='')
    for i in range(0, len(word)):
        if((i+1) % 3==0):
            print (".*..", end= '')
        else:
            print(".#..", end= '')
    print()

    #second line
    print('.', end='')
    for i in range(0, len(word)):
        if((i+1) % 3==0):
            print ("*.*.", end= '')
        else:
            print("#.#.", end='')

    print()

    #third line
    print('#', end='')
    for i in range(0, len(word)):
        print ("." + word[i] +".", end='')

        if(i%3!=0 and i!=len(word)-1):
            print("*", end='')
        elif(i!=len(word)-1):
            print("#", end='')

    if(len(word) % 3==0):
        print("*", end= '')
    else:
        print("#", end= '')

    print()


    #fourth line
    print('.', end='')
    for i in range(0, len(word)):
        if((i+1) % 3==0):
            print ("*.*.", end= '')
        else:
            print("#.#.", end='')

    print()

    #fifth line
    print('.', end='')
    for i in range(0, len(word)):
        if((i+1) % 3==0):
            print (".*..", end= '')
        else:
            print(".#..", end= '')
    print()

if __name__ == "__main__":
    main()