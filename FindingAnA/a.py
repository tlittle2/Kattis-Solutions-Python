

def main():
    word = input()
    idx= None
    for i in range(len(word)):
        if word[i] == 'a':
            idx = i
            break

    print(word[idx:len(word)])
    


if __name__ == "__main__":
    main()