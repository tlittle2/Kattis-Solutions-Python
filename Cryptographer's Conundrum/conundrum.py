def main():
    ip= input().strip()

    compare= 'PER'
    count= 0

    for i in range(len(ip)):
        if ip[i] != compare[i % 3]:
            count+=1
    print(count)
   
if __name__ == "__main__":
    main()
