import sys

#fails test cases even though the output for the test cases are correct
def main():
    stan = True

    for line in sys.stdin:
        limit = int(line)

        i = 1
        j = 2
        while i < limit:
            i*=j
            if j == 9:
                j = 2
            else:
                j+=1
            stan = not stan

        if stan:
            print("Stan wins.")
        else:
            print("Ollie wins.")
        
        stan = not stan

if __name__ == "__main__":
    main()
