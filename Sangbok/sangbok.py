def main():
    minutes, _ = map(int, input().split())
    minutes*=60

    songLengths = sorted(list(map(int, input().split())))        
    
    ans = 0
    for time in songLengths:
        if time > minutes:
            break
        ans+=time
        minutes-=time

    print(ans)

if __name__ == "__main__":
    main()
