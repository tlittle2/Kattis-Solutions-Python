def main():
    stk = []

    for _ in range(int(input())):
        stk.append(input()[::-1])

    while stk:
        print(stk.pop(), sep ="", end="")
              
if __name__ == "__main__":
    main()
