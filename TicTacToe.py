
#Implementation of Two Player Tic-Tac-Toe game in Python.

import sys
#We will make the board using dictionary

theBoard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}





board_keys=[]
for key in theBoard:
    board_keys.append(key)



#printboard
def printBoard(board):
    print(board['7']+ '|' +board['8'] +'|'+ board['9'])
    print('-+-+-')
    print(board['4']+ '|' +board['5'] +'|'+ board['6'])
    print('-+-+-')
    print(board['1']+ '|' +board['2'] +'|'+ board['3'])
    




#user_input
def game():
    turn='X'
    count = 0
    i=0

    while i<9:
        printBoard(theBoard)
        print('its your turn,'+turn+'.Move to which place?')
        move=input()
        if theBoard[move]==' ':
            theBoard[move]=turn
            count=count+1
            i=i+1
        else:
            print('that place is already filled. Move to which place?')
            continue
        
        if count>=5:# Now we will check if player X or O has won,for every move after 5 moves.
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['3']==theBoard['2']==theBoard['1']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['1']==theBoard['4']==theBoard['7']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['2']==theBoard['5']==theBoard['8']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['3']==theBoard['6']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['7']==theBoard['5']==theBoard['3']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
            elif theBoard['1']==theBoard['5']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("\n Game Over.\n")
                print('*** '+ turn+'won. ***')
                break
        if count==9:#If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            print("\n Game Over.\n")
            print("It's a tie!!")


        if turn=='X':
            turn='O'
        else:
            turn='X'
    

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key]=' '
        game()
    else:
        print('Thank you for your time!! hope you enjoyed!!!')
        sys.exit()
    
#main game calling
print('Hello Human ready to play a game!!!!!!!')
game()

          
        

    
    

    
