d = {
        '.': [20,0],
        'O': [10,0],
        '\\': [25,0],
        '/': [25,0],
        'A': [35,0],
        "^": [5,0],
        "v": [22,0]
    }

def main():
    rows, columns = map(int, input().split())
    
    for _ in range(rows):
        ip = list(input())
        for i in ip:
            d[i][1] += 1
    
    answer = 0
    for k, _ in d.items():
        answer += d[k][0] * d[k][1]
    
    print(answer)
if __name__ == "__main__":
    main()
