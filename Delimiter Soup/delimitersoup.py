def main():
    d = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    int(input())
    ip = input()
    stk = []
    badMatches = set()

    for i in range(len(ip)):
        if ip[i] in d.values(): #if current char is an opening delimiter, push it to the stack
            stk.append(ip[i])
        
        elif ip[i] in d.keys(): #if current char is a closing delimiter
            if stk and d[ip[i]] == stk[-1]: # and it's matching opening delimiter is at the top of the stack
                stk.pop() #pop opening delimiter off the stack
            else:
                badMatches.add("{} {}".format(ip[i], i)) #otherwise, add this match.
                break #Only want first occurrence, so break from here
    
    if badMatches:
        print("".join(badMatches))
    else:
        print("ok so far")
                        
if __name__ == "__main__":
    main()
