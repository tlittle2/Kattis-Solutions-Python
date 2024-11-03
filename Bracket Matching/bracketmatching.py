def main():
    d = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    stk = []

    int(input())
    ip = input()

    for i in range(len(ip)):
        if ip[i] in d.values(): #if current char is an opening delimiter, push it to the stack
            stk.append(ip[i])
        
        elif ip[i] in d.keys(): #if current char is a closing delimiter
            if stk and d[ip[i]] == stk[-1]: # and it's matching opening delimiter is currently at the top of the stack
                stk.pop() #pop opening delimiter off the stack
            else:
                stk.append(ip[i]) #otherwise, add it to the stack so that we don't forget that we had a closing delimiter with no open delimiter
    
    print("Invalid" if stk else "Valid") # if the stack has anything left after going through the input string, then it's not valid
                        
if __name__ == "__main__":
    main()
