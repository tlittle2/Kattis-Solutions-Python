def main():
    word = str(input())

    if word.count("b") == 0 and word.count("k") == 0:
        print("none")
    elif word.count("b") == word.count("k"):
        print("boki")
    elif word.count("b") > word.count("k"):
        print("boba") 
    elif word.count("b") < word.count("k"):
        print("kiki") 

if __name__ == "__main__":
    main() 
