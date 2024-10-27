def main():
    d = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    int(input())
    ip = input()
    stk = []
    val = set()

    for i in range(len(ip)):
        if ip[i] in d.values(): #if current char is an opening delimiter, push it to the stack
            stk.append(ip[i])
        
        elif ip[i] in d.keys(): #if current char is a closing delimiter
            if stk and d[ip[i]] == stk[-1]: # and it's matching opening delimiter is at the top of the stack
                stk.pop() #pop opening delimiter off the stack
            else:
                val.add("{} {}".format(ip[i], i))
        
        elif ip[i] != " ":
            val.add("{} {}".format(ip[i], i))
            

    if val:
        print("".join(val))
    else:
        print("ok so far")
                        
if __name__ == "__main__":
    main()
