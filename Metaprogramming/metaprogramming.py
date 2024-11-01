import sys

def main():
    d = dict()
    for line in sys.stdin:
        line = line.split()
        if line[0] == "define":
            d[line[2]] = int(line[1])
        else:            
            if line[1] not in d.keys() or line[3] not in d.keys():
                print("undefined")
            else:
                if line[2] == '=':
                    evalStatement = "{} {}= {}".format(d[line[1]], line[2], d[line[3]])
                else:
                    evalStatement = "{} {} {}".format(d[line[1]], line[2], d[line[3]])
                
                print("true" if eval(evalStatement) else "false")

if __name__ == "__main__":
    main()
