from GamePot import Pot
from GameBoard import Board


def showBoard(board):
    line1 = "  " + str(board.potArray[11].stoneNum) + " * " + str(board.potArray[10].stoneNum) + " * " + str(board.potArray[9].stoneNum) + " | " + str(board.potArray[8].stoneNum) + " * " + str(board.potArray[7].stoneNum) + " * " + str(board.potArray[6].stoneNum)
    line2 = str(board.storeP2) + "           |           " + str(board.storeP1)
    line3 = "  " + str(board.potArray[0].stoneNum) + " * " + str(board.potArray[1].stoneNum) + " * " + str(board.potArray[2].stoneNum) + " | " + str(board.potArray[3].stoneNum) + " * " + str(board.potArray[4].stoneNum) + " * " + str(board.potArray[5].stoneNum)
    line4 = "--------------------------------"
    print line1
    print line2
    print line3
    print line4

def main(textFile, numOfGames):

    winningMoveSets = []

    for i in range(0, numOfGames):
        numPerPot = 4
        potArray = [Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot),
                    Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot), Pot(numPerPot)]
        board = Board(potArray, 2)

        inGame = True
        while inGame:
            gameOver = board.test()
            # showBoard(board)
            if gameOver == 1:

                inGame = False
                if board.storeP2 > board.storeP1:
                    print "Player 2 Won"
                    winningMoveSets.append(board.player2MoveSet)
                    textFile.write("Player 2 Won")
                elif board.storeP1 > board.storeP2:
                    print "Player 1 Won"
                    winningMoveSets.append(board.player1MoveSet)
                    textFile.write("Player 1 Won")
                else:
                    print "Twas A Tie"
                    winningMoveSets.append(board.player1MoveSet)
                    winningMoveSets.append(board.player2MoveSet)
                    textFile.write("Twas A Tie")
                textFile.write("\n")
                break
                break
    return winningMoveSets

textFile = open("wins.txt", "w")
sets = main(textFile, 10)
textFile.close()





