def main():

    date = list(map(int, input().split('/')))

    if date[0] > 12: #if the first part of the date has a value greater than months in calendar, then that represents the number of days and it's European
        print("EU")
    elif date[1] > 12: #if the first part of the date has a value greater than months in calendar, then that represents the number of days and it's the US
        print("US")
    else: #otherwise it could be either
        print("either")


if __name__ == "__main__":
    main()
