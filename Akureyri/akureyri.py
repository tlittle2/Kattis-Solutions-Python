def main():
    d = dict()

    for i in range(int(input()) * 2):
        city = input()
        if i % 2 == 1:
            if city in d.keys():
                d[city] += 1
            else:
                d[city] = 1
    
    for i in sorted(d):
        print("{} {}".format(i, d[i]))

    
if __name__ == "__main__":
    main()
