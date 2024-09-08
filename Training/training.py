def main():
    p, skill = map(int, input().split())
    
    for _ in range(p):
        low, high = map(int, input().split())
        if low <= skill <= high:
            skill+=1
    
    print(skill)
    
if __name__ == "__main__":
    main()
