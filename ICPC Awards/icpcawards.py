def main():
    s = set()
    l = list()
    
    for _ in range(int(input())):
        college, team = input().split()
        if college not in s: 
            s.add(college)
            l.append("{} {}".format(college, team))

    for i in l[0:12]: #get the top 12
        print(i)

if __name__ == "__main__":
    main()
