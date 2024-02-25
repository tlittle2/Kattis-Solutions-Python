def main():
    ip = list(map(str, input().split()))
    
    title = ip[0]
    cost = float(ip[1])

    length = len(title)

    if cost < length:
        print(cost)
    else:
        print(length)

if __name__ == "__main__":
    main() 
