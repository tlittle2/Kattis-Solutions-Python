def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    month_start = {
        6: 0,
        2: 6, 3: 6, 11: 6,
        1: 3, 10: 3,
        9: 1, 12: 1,
        5: 4,
        8: 5,
        4: 2, 7: 2
    }

    d, m = map(int, input().split())

    print(days[(month_start.get(m, 0) + d - 1) % 7])


if __name__ == "__main__":
    main()
