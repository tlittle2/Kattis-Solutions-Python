def main():
    values = list(map(int, input().split()))
    print(values[0] * values[2] + (0.5 * values[1] * values[2] ** 2))

if __name__ == "__main__":
    main()
