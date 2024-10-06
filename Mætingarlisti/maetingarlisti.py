def main():
    n,r,c = map(int, input().split())

    ourClass = []

    #create 2d array out of the rows in the classroom
    for _ in range(r):
        ourClass.append(input().split())
    
    #in groups of r by c
    for i in range(r):
        myRow = [input() for _ in range(c)] #append to temp rows to compare against
        
        if ourClass[i] == myRow: #see if the templist is exactly equal to the corresponding row from the class
            print("left")
        else:
            print("right")

if __name__ == "__main__":
    main()
