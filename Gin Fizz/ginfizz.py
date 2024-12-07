def main():
    d = {
        "ml gin": 45,
        "ml fresh lemon juice": 30,
        "ml simple syrup": 10,
    }

    ginfizz = int(input())
    
    for k,v in d.items():
        print("{} {}".format(v * ginfizz, k))
    
    if ginfizz == 1:
        print("{} slice of lemon".format(ginfizz))
    else:
        print("{} slices of lemon".format(ginfizz))

if __name__ == "__main__":
    main()
