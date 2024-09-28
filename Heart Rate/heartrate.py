def main():
    for _ in range(int(input())):
        b,p = input().split()
        b = int(b)
        p = float(p)
        bpm = round((60 * b) / p,4)

        print(round(bpm - (60/p),4), bpm, round(bpm + (60/p),4))

if __name__ == "__main__":
    main()
