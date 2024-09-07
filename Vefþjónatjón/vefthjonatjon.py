"""
Is there a better solution than this?
"""
def main():
    lst = []

    c = 0
    m = 0
    h = 0

    for _ in range(int(input())):
        ip = input().split()
        if ip[0] == 'J':
            c+=1
        if ip[1] == 'J':
            m+=1
        if ip[2] == 'J':
            h+=1 
    min = 10000
    if(c < min):
        min = c
    if(m < min):
        min = m
    if (h < min):
        min = h
    
    print(min)

if __name__ == "__main__":
    main()
