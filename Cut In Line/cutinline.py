def main():
    q = [input() for _ in range(int(input()))]

    for _ in range(int(input())):
        o = input().split()

        if o[0] == "leave":
            q.remove(q[q.index(o[1])])
        else:
            q.insert(q.index(o[2]), o[1])
        
    for i in q:
        print(i)

if __name__ == "__main__":
    main()
