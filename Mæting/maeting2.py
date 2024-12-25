#Doesn't work in Kattis -> requires pip3 install of ordered_set
from ordered_set import OrderedSet

def main():
    _ =input().split()

    ip1 = list(map(int, input().split()))
    ip2 = list(map(int, input().split()))

    seen = OrderedSet()

    for i in ip1:
        if i in ip2:
            seen.add(i)
    
    for i in seen:
        print(i, sep = " ", end =" ")


if __name__ == "__main__":
    main()
