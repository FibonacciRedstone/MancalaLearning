import ast

from Board import Board
from Player import Player
from Pot import Pot


def createPlayerFromFile(fileName):
    textFile = open(fileName, "r")
    dictionary = ast.literal_eval(textFile.readline())
    winsLine = textFile.readline()
    wins = winsLine[16:]
    textFile.close()
    player = Player()
    player.stateMoveDictionary = dictionary
    player.reInitDict()
    player.winsAmount = wins
    return player


def showBoard(board):
    line1 = "  " + str(board.potArray[11].stoneNum) + " * " + str(board.potArray[10].stoneNum) + " * " + str(
        board.potArray[9].stoneNum) + " | " + str(board.potArray[8].stoneNum) + " * " + str(
        board.potArray[7].stoneNum) + " * " + str(board.potArray[6].stoneNum)
    line2 = str(board.storeP2) + "           |           " + str(board.storeP1)
    line3 = "  " + str(board.potArray[0].stoneNum) + " * " + str(board.potArray[1].stoneNum) + " * " + str(
        board.potArray[2].stoneNum) + " | " + str(board.potArray[3].stoneNum) + " * " + str(
        board.potArray[4].stoneNum) + " * " + str(board.potArray[5].stoneNum)

    print line1
    print line2
    print line3


def main():
    computer = createPlayerFromFile("bestway.txt")
    potArray = [Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot()]
    board = Board(potArray, computer)

    inGame = True
    while inGame:
        gameOver = board.test()
        showBoard(board)
        if gameOver == 1:
            if board.storeP2 > board.storeP1:
                print "Player 2 Won"
            elif board.storeP1 > board.storeP2:
                print "Player 1 Won"
            else:
                print "Twas A Tie"
            break


main()
