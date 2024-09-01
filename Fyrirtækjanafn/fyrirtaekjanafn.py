def main():
    vowels = ['a','e','i','o','u','y']
    w = ""
    for i in input():
        if i.lower() in vowels:
            w+=i
    print(w) 
if __name__ == "__main__":
    main()
