def main():
    int(input())
    temps = list(map(int, input().split()))
    print("{} {}".format(max(temps), min(temps)))
        
if __name__ == "__main__":
    main()
