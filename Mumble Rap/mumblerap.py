import re

#Partially Accepted
def main():
    int(input())
    numbers = re.findall(r"\d+", input())
    print(max(numbers))

if __name__ == "__main__":
    main()
