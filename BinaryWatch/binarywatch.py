#/bin/usr/env python3

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


def rowstoColumns(l, counter):
    pass



def main():
    ip = input()
    lst = list()

    #get all of the correct binary values and store them into a list (each value will have its own indice``)
    for i in ip:
        lst.append(binaries[i])


    #convert to rows to make it easier to print the output that kattis wants
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    
    for i in range(len(lst)):
        row1+=lst[i][0]
        row2+=lst[i][1]
        row3+=lst[i][2]
        row4+=lst[i][3]

    print("{} {}   {} {}".format(row1[0], row1[1], row1[2], row1[3]))
    print("{} {}   {} {}".format(row2[0], row2[1], row2[2], row2[3]))
    print("{} {}   {} {}".format(row3[0], row3[1], row3[2], row3[3]))
    print("{} {}   {} {}".format(row4[0], row4[1], row4[2], row4[3]))


    








if __name__ == "__main__":
    main()