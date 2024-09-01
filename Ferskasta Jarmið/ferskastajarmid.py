def main():
    d = {}

    for _ in range(int(input())):
        ip = input().split()
        d[ip[0]] = int(ip[1]) * int(ip[2])

    max_keys = sorted([key for key, value in d.items() if value == max(d.values())]) #get the maximum value of the values in the dictionary, and acquire all keys with that max value. sort the list

    print(max_keys[0]) #get the key that is the earliest in the alphabet that has that max value

if __name__ == "__main__":
    main()
