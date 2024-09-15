def main():
    #Make number a list of digits
    a = [int(i) for i in input()]
    b = [int(i) for i in input()]

    #add 0s to the front of the smaller list if required to make sure number comparisons are the same
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b

    #Main logic of the problem
    mstrA = []
    mstrB = []
    for i in range(len(a)):
        if a[i] == b[i]: #if numbers are the same, consider both numbers
            mstrA.append(a[i])
            mstrB.append(a[i])
        elif a[i] > b[i]:
            mstrA.append(a[i])
        else:
            mstrB.append(b[i])

    #printing output
    if len(mstrA) == 0:
        print("YODA")
    else:
        print(int(''.join(map(str, mstrA))))

    if len(mstrB) == 0:
        print("YODA")
    else:
        print(int(''.join(map(str, mstrB))))

if __name__ == "__main__":
    main()
