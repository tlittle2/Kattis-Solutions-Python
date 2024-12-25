def main():   
    n = int(input())

    for i in range(1, n+1):
        d = {}
        int(input())
        cases = map(int, input().split())
        for j in cases:
            if j not in d.keys():
                d[j] = 1
            else:
                d[j] +=1

        print("Case #{}: {}".format(i, list(filter(lambda x: d[x] == 1, d))[0]))

if __name__ == "__main__":
    main()
