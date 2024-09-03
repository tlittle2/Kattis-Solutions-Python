def main():
    for _ in range(int(input())):
        s = set()
        l = []
        cases = int(input())
        totalVotes = 0
        for _ in range(cases):
            v = int(input())
            totalVotes += v
            s.add(v)
            l.append(v)
        if len(s) == 1:
            print("no winner") #if all inputs are the same, we don't have a winner
        else:
            mx = max(l)
            if l.count(mx) > 1: #if there are ties on the max, we don't have a winner
                print("no winner")
            elif mx > totalVotes / 2: #majority vote calculation
                print("majority winner {}".format(l.index(mx) + 1))
            else:
                print("minority winner {}".format(l.index(mx) + 1))

if __name__ == "__main__":
    main()
