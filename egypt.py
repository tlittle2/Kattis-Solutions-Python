import sys

def main():
    for i in sys.stdin:
        inputs = sorted(list(map(int, i.split())))
        if inputs[0] == 0 and inputs[1] == 0 and inputs[1] == 0:
            break
        if inputs[0] **2 + inputs[1] **2 == inputs[2] **2:
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    main() 
