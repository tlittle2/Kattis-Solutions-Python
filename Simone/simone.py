def main():
    d = {}
    possibleColors = input().split()[1]

    for i in range(1,int(possibleColors)+1): #initialize all keys to have a value of 0, and increment later
        d[str(i)] = 0

    for i in input().split(): #for each color from the input that has a corresponding key, increment the value
        d[i] +=1

    vals = []
    
    for k, v in d.items():
        if v == min(d.values()): #retrieve all keys where the value is equal to the number(s) that occurs the least often
            vals.append(int(k))
    
    if len(vals) > 0: #if we have stuff to print out, print it
        print(len(vals))
        for i in vals:
            print("{}".format(i), sep = "", end = " ")
            
if __name__ == "__main__":
    main()
