def main():
    a, b = map(int, input().split())

    c, d= map(int, input().split())

    charge= int(input())

    distance= abs(a-c) + abs(b-d)

    if(charge - distance) % 2 == 0 and (charge >=distance):
        print('Y')
    else:
        print('N')

if __name__ == "__main__":
    main()
