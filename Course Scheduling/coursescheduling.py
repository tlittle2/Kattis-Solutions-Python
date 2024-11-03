def main():
    enrollments = dict()
    
    for _ in range(int(input())):
        entry = input().split()
        name = "{} {}".format(entry[0],entry[1]) 
        clss = entry[2]
        if clss not in enrollments:
            enrollments[clss] = {name}
        else:
            enrollments[clss].add(name)

    for k,v in sorted(enrollments.items()):
        print("{} {}".format(k, len(v)))
        
if __name__ == "__main__":
    main()
