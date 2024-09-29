#output is the same, but is not getting accepted
def main():
    percent,length = map(int, input().split())

    hashtags = round((percent * length) / 100)

    print("[", sep = "", end = "")
    print("".join(["#" for _ in range(hashtags)]), sep = "", end = "")
    print("".join(["-" for _ in range(length - hashtags)]), sep = "", end = "")
    print("{} {} {}".format("]", "|","{:>3}%".format(percent)), sep = "", end = "")
    
if __name__ == "__main__": 
    main()
