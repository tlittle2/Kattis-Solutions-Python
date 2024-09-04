import math

def main():
    ips = list(map(int, input().split()))
    diagonal = int(math.sqrt(ips[1]**2 + ips[2]**2))

    for _ in range(ips[0]):
        if int(input()) <= diagonal:
            print("DA")
        else:
            print("NE")
                
if __name__ == "__main__":
    main()
