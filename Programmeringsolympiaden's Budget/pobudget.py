def main():
    cases = int(input())

    ans = 0
    for i in range(cases * 2):
        if i % 2 == 1:
            ans+=int(input())
        else:
            input()

    if ans > 0:
        print("Usch, vinst")
    elif ans < 0:
        print("Nekad")
    else:
        print("Lagom")
    
if __name__ == "__main__": 
    main()
