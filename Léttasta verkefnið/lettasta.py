def main():
    problems = int(input())
    teams = int(input())

    names = input().split()

    problemMap = {i: names[i] for i in range(problems)}

    scoreMap = {i: 0 for i in range(problems)}
    
    for i in range(teams):
        ip = list(map(int,input().split()))
        for i in range(problems):
            scoreMap[i] += ip[i]
    
    print(problemMap[max(scoreMap, key=scoreMap.get)])
    

if __name__ == "__main__":
    main()
