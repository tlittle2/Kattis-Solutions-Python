def main():
    int(input())
    l = list(map(int, input().split()))
    
    print(int(sum(i for i in l)/len(l)))

if __name__ == "__main__":
    main() 
