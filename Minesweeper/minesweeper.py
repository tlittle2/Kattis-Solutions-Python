def main():
    rows, columns, ips = map(int, input().split())
    board = []

    #make board of all '.' based on initial input
    for _ in range(columns):
        board.append(list('.' * rows))

    #update the board for mines based on data from stdin
    for _ in range(ips):
        upRow, upCol = map(int, input().split())
        board[upCol-1][upRow-1] = '*'

    #tranpose the board (make columns into rows) and print out each list from that
    for k in [list(i) for i in zip(*board)]:
        print(''.join(k))
      
if __name__ == "__main__":
    main()
