"""
This is a stack question because you have to back track to get answers as you loop through the input
"""
def main():
    ans = set()
    s = []
    for _ in range(int(input())):
        ip = input()
        if ip != "Present!":
            ans.add(ip)
            s.append(ip)
        else:
            ans.add(s.pop())
    if len(s) == 0:
        print("No Absences")
    else:
        for i in s:
            print(i)

if __name__ == "__main__":
    main()
