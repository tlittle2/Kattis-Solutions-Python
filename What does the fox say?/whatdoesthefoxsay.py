def main():
    s = set()
    for _ in range(int(input())):
        ip = input().split()
        output = ""

        while True:
            translate = input()
            if translate == "what does the fox say?":
                break
            else:
                _, _, sound = translate.split()
                s.add(sound)
                        
        for i in ip:
            if i not in s:
                output+="{} ".format(i)
        
        print(output)

if __name__ == "__main__":
    main()
