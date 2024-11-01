def main():
    numOfWords = int(input())

    words = set(input().lower() for _ in range(numOfWords))
    
    sentence = input().lower().split()

    print("Hi, how do I look today?" if all(word in words for word in sentence) else "Thore has left the chat")

if __name__ == "__main__":
    main()
