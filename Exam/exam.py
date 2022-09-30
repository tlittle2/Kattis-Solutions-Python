#!/usr/bin/env python3

def main():
    fs = int(input())
    myanswers= input()
    fanswers = input()

    matching = 0
    for i in range(len(myanswers)):
        if myanswers[i] ==  fanswers[i]:
            matching+=1

    
    if matching >= fs:
        print(fs + (len(myanswers) - matching))
    else:
        print(matching + (len(myanswers) - fs))




if __name__ == "__main__":
    main()