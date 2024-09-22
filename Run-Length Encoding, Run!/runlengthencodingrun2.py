def encode(s):
    newString = ""
    c = 0
    startLetter = s[0]

    for i in range(len(s)):
        if s[i] == startLetter:
            c+=1
        else:
            newString+=startLetter + str(c)
            startLetter = s[i]
            c = 1
    newString+=startLetter + str(c)
        
    return newString

def main():
    m, s = input().split()

    if m == "D":
        print(''.join([s[i]*int(s[i+1]) for i in range(0, len(s)-1, 2)]))
    if m == "E":
        print(encode(s))

if __name__ == "__main__":
    main()
