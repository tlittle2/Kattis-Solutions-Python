def main():
    d = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    int(input())
    ip = input()
    stk = [""] #initialize stack with dummy value to always make sure we have something to compare against
    val = set()

    for i in range(len(ip)):
        if ip[i] in d.values(): #if current char is an opening delimiter, push it to the stack
            stk.append(ip[i])
        elif ip[i] in d.keys() and d[ip[i]] == stk[-1]: #if current char is a closing delimiter and it's matching opening delimiter is at the top of the stack
            stk.pop() #pop (what would be the opening delimiter) off the stack
            
            if len(stk) == 0: #append dummy value if the stack ever gets empty to ensure we have something to compare against
                stk.append("")
        else:
            if ip[i] != " ":
                val.add("{} {}".format(ip[i], i))
        
    if len(val) >= 1:
        print("".join(val))
    else:
        print("ok so far")
                        
if __name__ == "__main__":
    main()
