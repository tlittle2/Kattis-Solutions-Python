def main():
    s1 = sum(map(int, input().split()))
    s2 = sum(map(int, input().split()))

    if s2 > s1:
        print("Emma")
    elif s2 < s1:
        print("Gunnar")
    else:
        print("Tie")


if __name__ == "__main__": 
    main()
