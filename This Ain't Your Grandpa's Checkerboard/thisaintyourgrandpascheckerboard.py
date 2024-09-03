def main():
    numOfLines= int(input())
    board= []
    b= False
    for i in range(numOfLines):
        column= [x for x in input().strip()]
        board.append(column)

    #check rows
    for i in range(len(board)):
        if board[i].count('B') != board[i].count('W'):
            b= True
            break
        for j in range(len(column)-2):
            if board[i][j] == 'B' and board[i][j+1]== 'B' and board[i][j+2] =='B' :
                b= True
                break
            if board[i][j] == 'W' and board[i][j+1]== 'W' and board[i][j+2] =='W' :
                b= True
                break


    #check columns
    for i in range(len(board)):
        tally = 0
        for j in range(len(column)):
            if(board[i][j] == 'B'):
                tally+=1
            else:
                tally-=1

        if tally != 0:
                b= True
                break
        
        for j in range(len(column)-3):
            if board[j][i] == 'B' and board[j+1][i]== 'B' and board[j+2][i] =='B' :
                b= True
                break
            if board[j][i] == 'W' and board[j+1][i]== 'W' and board[j+2][i] =='W' :
                b= True
                break
            
    if b== True:
        print(0)
    else:
        print(1)
    
if __name__ == "__main__":
    main()
