def main():
    ip = input()
    length = len(ip) // 3
    l = []

    t = 0
    while t < len(ip):
        l.append(ip[t:t+length])
        t+=length

    d = {i : l.count(i) for i in l}
    print(''.join(k for k,v in d.items() if v > 1))

if __name__ == "__main__":
    main()
