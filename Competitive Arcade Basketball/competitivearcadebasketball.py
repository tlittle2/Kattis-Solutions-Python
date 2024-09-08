def main():
    d = {}
    
    ip = list(map(int, input().split()))

    for _ in range(ip[0]):
        d[input()] = 0
    
    for i in range(ip[2]):
        name,points = input().split()
        d[name] += int(points)

    
    winners = [k for k,v in d.items() if v>= ip[1]]

    if len(winners) == 0:
        print("No winner!")
    else:
        for i in winners:
            print("{} wins!".format(i))

if __name__ == "__main__":
    main()
