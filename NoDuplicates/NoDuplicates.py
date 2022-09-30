#/usr/bin/env python3
import sys

def main():
    ip= str(sys.stdin.readline().strip())

    words= ip.split(" ")
    ipList= []
    for i in range(len(words)):
        ipList.append(words[i])

    wordIterator= " "
    currentComparison= " "

    boolean= False

    for i in range(0, (len(ipList)-1), 1):
        if(ipList.count(ipList[i]) > 1):
                boolean= True
                break

    if boolean== True:
        print("no")
    else:
        print("yes")

if __name__ == "__main__":
    main()