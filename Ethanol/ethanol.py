def formatOutput(c, n):
    initial = "  {}".format(c)
    return initial if n == 1 else "{} {}".format(initial, (c + " ") *(n-1))


def main():
    n = int(input())
    hydrogen = "H"
    pipe = "|"
    
    print(formatOutput(hydrogen,n))
    print(formatOutput(pipe,n))
    print("{}-{}{}".format(hydrogen,"C-"*n if n>1 else "C", "OH" if n>1 else "-OH"))
    print(formatOutput(pipe,n))
    print(formatOutput(hydrogen,n))
    
        
if __name__ == "__main__": 
    main()
