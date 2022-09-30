#/usr/bin/env/python3

def main():
    log = ' '
    rightProblems = []
    wrongProblems = []

    rightNumbers = []

    time = 0
    numberWrong = 0



    while log!= '-1':
        log= input()
        if log != '-1':
            if 'right' in log.split() and not (log.split()[1] in rightNumbers):
                rightProblems.append(log.split())
                rightNumbers.append(log.split()[1])
                time+=int((log.split()[0]))
            else:
                wrongProblems.append(log.split())
                


    for i in rightProblems:
        for j in wrongProblems:
            if j[1] == i[1]:
                time += 20
            
    print(len(rightProblems), time)	

if __name__ == "__main__":
    main()