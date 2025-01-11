def main():
    radius, crust = map(int, input().split())

    print((float((radius-crust)**2) /radius/radius) * 100)

if __name__ == "__main__":
    main()
