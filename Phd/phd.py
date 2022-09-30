#!/usr/bin/env python3

def main():
    for i in range(int(input())):
        s = input()
        if s == "P=NP":
            print("skipped")
            continue
        else:
            a = eval(s)
            print(a)
        




if __name__ == "__main__":
    main()