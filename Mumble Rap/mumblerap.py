import re

def main():
    int(input())
    numbers = list(map(int,re.findall(r"\d+", input())))
    print(max(numbers))
                        
if __name__ == "__main__":
    main()
