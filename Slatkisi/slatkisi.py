def main():
    dollars, zeros = map(int, input().split())

    r = "1"

    for _ in range(zeros):
        r +="0"

    print(round(dollars / int(r)) * int(r))   

if __name__ == "__main__": 
    main()
