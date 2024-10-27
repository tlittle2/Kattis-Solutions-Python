import re

#Partially Accepted
def main():
    int(input())
    ip = input()
    numbers = re.findall(r"\d+", ip)
    print(max(numbers))
                        
if __name__ == "__main__":
    main()
