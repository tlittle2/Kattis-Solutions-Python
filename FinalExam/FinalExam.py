def main():
    n= int(input())

    correct= []
    for i in range(n):
        answer= input()
        correct.append(answer)
    
    myAnswers= []
    for i in range(1, len(correct)):
        myAnswers.append(correct[i])

    count=0
    for i in range(len(correct) -1):
        if correct[i] == myAnswers[i]:
            count+=1

    print(count)

if __name__ == "__main__":
    main()
