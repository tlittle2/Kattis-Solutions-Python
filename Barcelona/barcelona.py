def main():
    values = list(map(int, input().split()))
    bags = list(map(int, input().split()))

    if values[1] == bags[0]:
        print("fyrst")
    elif values[1] == bags[1]:
        print("naestfyrst")
    else:
        print("{} fyrst".format(bags.index(values[1])+1))
    


if __name__ == "__main__":
    main()
