def main():
    rows, cols = map(int, input().split())

    matrix = [list(input()) for _ in range(rows)]

    transposed = [list(row) for row in zip(*matrix)] #change rows to columns

    for i in range(len(transposed)):
        latest = len(transposed[i])-1
        for j in range(len(transposed[i])-1, -1,-1):
            if transposed[i][j] == 'S': #if current index is a snowflake, move snowflake to the latest index that has '.'
                transposed[i][j] = '.'
                transposed[i][latest] = 'S'
                latest-=1
    
    changeBack = [list(cols) for cols in zip(*transposed)] #change matrix back to how we received from stdin

    for i in changeBack: #print out the new graph
        print(''.join(i))


if __name__ == "__main__":
    main()
