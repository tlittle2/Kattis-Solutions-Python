import sys

def main():
    for line in sys.stdin:
        print("yes" if "problem" in line.lower() else "no")

if __name__ == "__main__":
    main()
