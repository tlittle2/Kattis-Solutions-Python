def main():
    d = {
        "ml gin": 45,
        "ml fresh lemon juice": 30,
        "ml simple syrup": 10,
        "slice of lemon": 1
    }

    ginfizz = int(input())
    
    if ginfizz > 1: #make a copy of the key to be plural and remove the old key
        d["slices of lemon"] = d["slice of lemon"]
        del d["slice of lemon"]

    for k,v in d.items():
        print("{} {}".format(v * ginfizz, k))


if __name__ == "__main__":
    main()
