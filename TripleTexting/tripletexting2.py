def main():
    ip = input()
    length = len(ip) // 3
    l = []

    t = 0
    while t < len(ip): #process input
        l.append(ip[t:t+length])
        t+=length

    d = {i : l.count(i) for i in set(l)} #generate occurrence map
    print(''.join(k for k,v in d.items() if v > 1)) #print the word(s) that occur more than 1 time

if __name__ == "__main__":
    main()
