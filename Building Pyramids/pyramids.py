def main():
    blocks = int(input())
    tmp = 0
    i = 1
    j = 0

    while tmp < blocks:
        tmp+= i*i
        i+=2
        j+=1
      
    print(j-1 if tmp > blocks else j)
  
if __name__ == "__main__":
    main()
