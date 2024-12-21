def main():
    problems, totalProblems = map(int,input().split())

    d= {i: 0 for i in range(1,problems+1)}

    for _ in range(totalProblems):
        _, p = map(int,input().split())
        d[p] +=1

    print(min(d.values()))
    
    
if __name__ == "__main__": 
    main()
