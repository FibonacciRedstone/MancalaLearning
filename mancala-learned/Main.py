from GamePot import Pot
from GameBoard import Board


def showBoard(board):
    line1 = "  " + str(board.potArray[11].stoneNum) + " * " + str(board.potArray[10].stoneNum) + " * " + str(board.potArray[9].stoneNum) + " | " + str(board.potArray[8].stoneNum) + " * " + str(board.potArray[7].stoneNum) + " * " + str(board.potArray[6].stoneNum)
    line2 = str(board.storeP2) + "           |           " + str(board.storeP1)
    line3 = "  " + str(board.potArray[0].stoneNum) + " * " + str(board.potArray[1].stoneNum) + " * " + str(board.potArray[2].stoneNum) + " | " + str(board.potArray[3].stoneNum) + " * " + str(board.potArray[4].stoneNum) + " * " + str(board.potArray[5].stoneNum)

    print line1
    print line2
    print line3

def main():
    numPerPot = 4
    potArray = [Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot)]
    board = Board(potArray, 3)

    inGame = True
    while inGame:
        gameOver = board.test()
        showBoard(board)
        if gameOver == 1:
            inGame = False
            if board.storeP2 > board.storeP1:
                print "Player 2 Won"
            elif board.storeP1 > board.storeP2:
                print "Player 1 Won"
            else:
                print "Twas A Tie"
            break


main()





