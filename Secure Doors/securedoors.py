
def main():
    #data structure: name, [entered (Boolean), exited(boolean)]
    d = {}

    for _ in range(int(input())):
        s = input().split()
        name = s[1]
        status = s[0]
      
        if name not in d.keys(): #if person doesn't exist in the dictionary, put them in
            if status == "entry":
                print("{} entered".format(name))
                d[name] = [True, False]
            else:
                print("{} exited (ANOMALY)".format(name)) #you cannot exit if you never entered
                d[name] = [False, True]
        else:
            if status == "entry":
                if d[name][0]: #you can't enter if you never exited
                    print("{} entered (ANOMALY)".format(name))
                else:
                    print("{} entered".format(name))
                    d[name] = [True, False]

            elif status == "exit":
                if d[name][1]:  #you can't exit if you never entered
                    print("{} exited (ANOMALY)".format(name))
                else:
                    print("{} exited".format(name))
                    d[name] = [False, True]


if __name__ == "__main__":
    main()
