def formatOutput(c, n):
    return f"  {c}" + f" {(c + ' ') * max(0, n - 1)}"


def main():
    n = int(input())
    hydrogen = "H"
    pipe = "|"
    
    print(formatOutput(hydrogen,n))
    print(formatOutput(pipe,n))
    print(f"{hydrogen}-"f"{'C-'*n}OH")
    print(formatOutput(pipe,n))
    print(formatOutput(hydrogen,n))
    
        
if __name__ == "__main__": 
    main()
