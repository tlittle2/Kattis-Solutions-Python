def main():
    sentence = input() + " "
    output = ""

    for i in range(len(sentence)-1):
        if sentence[i] != sentence[i+1]:
            output+=sentence[i]

    print(output)

if __name__ == "__main__":
    main()
