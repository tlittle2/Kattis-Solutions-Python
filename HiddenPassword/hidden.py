#/usr/bin/env python3



def main():
    key, seq = input().split()
    blank = ""
    d = {}

    for i in seq:
        if i in key:
            if i not in blank or blank.count(i) < key.count(i):
                blank+=i


    if blank == key:
        print("PASS")
    else:
        print("FAIL")




if __name__ == "__main__":
    main()