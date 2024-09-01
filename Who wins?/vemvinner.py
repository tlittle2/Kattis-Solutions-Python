def determineWinner(list, char):
    for sublist in list:
        if all(c == char for c in sublist):
            return True
    return False

def main():
    l = [list(input().split()) for _ in range(3)] #make 2d list of data from stdin
    horizontal = l #the data from the original list is all the horizontals
    vertical = list(zip(*l)) #group all index 0s, index 1s, and index 2s together to form all verticals
    leftDiagonal = [(l[0][0],l[1][1],l[2][2])]
    rightDiagonal = [(l[0][2],l[1][1],l[2][0])]

    johanWin = determineWinner(horizontal, 'X') or determineWinner(vertical, 'X') or determineWinner(leftDiagonal, 'X') or determineWinner(rightDiagonal, 'X')
    AbdullahWin = determineWinner(horizontal, 'O') or determineWinner(vertical, 'O') or determineWinner(leftDiagonal, 'O') or determineWinner(rightDiagonal, 'O')

    if not johanWin and not AbdullahWin:
        print("ingen har vunnit")
    else:
        if johanWin:
            print("Johan har vunnit")
        else:
            print("Abdullah har vunnit")

if __name__ == "__main__":
    main()
