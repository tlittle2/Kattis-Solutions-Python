#/usr/bin/env python3


def main():
    corr = [4,3,2,7,6,5,4,3,2,1]

    integers = []
    s = input()
    for c in s:
        integers.append(c)
    

    integers.remove('-')

    #print(integers)

    answers= []
    for i in range(len(integers)):
        answers.append(int(integers[i]) * corr[i]) 


    final = 0

    for n in answers:
        final+=n

    if final % 11 == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()