import itertools
import math
from datetime import datetime

from GameBoard import Board
from GamePot import Pot
from Player import Player

global currentIndex


def showBoard(board):
    line1 = "  " + str(board.potArray[11].stoneNum) + " * " + str(board.potArray[10].stoneNum) + " * " + str(
        board.potArray[9].stoneNum) + " | " + str(board.potArray[8].stoneNum) + " * " + str(
        board.potArray[7].stoneNum) + " * " + str(board.potArray[6].stoneNum)
    line2 = str(board.storeP2) + "           |           " + str(board.storeP1)
    line3 = "  " + str(board.potArray[0].stoneNum) + " * " + str(board.potArray[1].stoneNum) + " * " + str(
        board.potArray[2].stoneNum) + " | " + str(board.potArray[3].stoneNum) + " * " + str(
        board.potArray[4].stoneNum) + " * " + str(board.potArray[5].stoneNum)
    line4 = "--------------------------------"
    print line1
    print line2
    print line3
    print line4


def main(numOfGames):
    global gameStates
    gameStates = generateGameStates()

    winningPlayerArray = []

    for i in range(0, numOfGames):
        potArray = createPotArray()
        board = Board(potArray)
        battleVar = battle(board, Player(), Player())
        if battleVar[0].stateMoveDictionary != {}:
            winningPlayerArray.append(battleVar[0])
        if battleVar[1].stateMoveDictionary != {}:
            winningPlayerArray.append(battleVar[1])
    print "Initial Games Completed"
    roundNum = 0
    winningPlayerAmount = 3
    while winningPlayerAmount > 2:
        roundNum += 1
        combs = battleCombinations(winningPlayerArray)
        winningPlayerArray = getTopPlayers(combs)
        winningPlayerAmount = len(winningPlayerArray)
        print "Round " + str(roundNum) + " Finished"
    if len(winningPlayerArray) == 2:
        if winningPlayerArray[0].winsAmount > winningPlayerArray[1].winsAmount:
            return winningPlayerArray[0]
        else:
            return winningPlayerArray[1]
    elif len(winningPlayerArray) == 1:
        return winningPlayerArray[0]


def battleCombinations(players):
    j = 1
    newPlayerArray = []
    while len(players) != 0:
        while j < len(players):
            potArray = createPotArray()
            board = Board(potArray)

            player1 = players[0]
            if player1.stateMoveDictionary.values()[0] > 5:
                for state in gameStates:
                    player1.stateMoveDictionary[tuple(state)] -= 6
            player2 = players[j]
            if player2.stateMoveDictionary.values()[0] < 6:
                for state in gameStates:
                    player2.stateMoveDictionary[tuple(state)] += 6
            newPlayerTuple = battle(board, player1, player2)

            for player in newPlayerTuple:
                if not player in newPlayerArray:
                    newPlayerArray.append(player)
            j += 1
        del players[0]
        j = 1
    return newPlayerArray


def getTopPlayers(inputPlayers):
    choosingPercent = .5
    outputSize = int(math.floor(len(inputPlayers) * choosingPercent))
    outputPlayers = []
    currentMax = Player()
    currentMaxIndex = 0
    for i in range(0, outputSize):
        for j in range(0, len(inputPlayers)):
            if inputPlayers[j].winsAmount > currentMax:
                currentMax = inputPlayers[j]
                currentMaxIndex = j
        del inputPlayers[currentMaxIndex]
        outputPlayers.append(currentMax)
    i = 0
    while i < len(outputPlayers):
        if outputPlayers[i].winsAmount == 0:
            outputPlayers.remove(outputPlayers[i])
        i += 1

    return outputPlayers


def createPotArray():
    pots = [Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot(), Pot()]
    return pots


def battle(board, player1, player2):
    wins = []
    inGame = True
    while inGame:
        gameOver = board.test(player1, player2)
        if gameOver == 1:

            if board.storeP2 > board.storeP1:
                print "Player 2 Won"
                player2.winsAmount += 1
            elif board.storeP1 > board.storeP2:
                print "Player 1 Won"
                player1.winsAmount += 1
            else:
                print "Twas A Tie"
                player1.winsAmount += 1
                player2.winsAmount += 1

            return player1, player2
            break
            break
    return wins


def getPermutations(inputArray, interable):
    perms = list(itertools.permutations(inputArray, interable))
    returnPerms = list()

    for permutation in perms:
        if len(returnPerms) > 0:
            keepPerm = True
            for perm in returnPerms:
                if perm == permutation:
                    keepPerm = False
                    break
            if keepPerm:
                returnPerms.append(permutation)
        else:
            returnPerms.append(permutation)
    return returnPerms


def generateGameStates():
    gameStates = []

    permList = [0, 0, 0, 0, 0, 0]
    for i in range(0, 6):
        comb = getPermutations(permList, 6)
        for perm in comb:
            gameStates.append(perm)
        permList[i] = 1
    gameStates.append(permList)
    del gameStates[0]
    return gameStates


def run(startingAmount):
    startTime = datetime.now()
    textFile = open("bestway.txt", "w")
    set = main(startingAmount)
    textFile.write(str(set.stateMoveDictionary))
    textFile.write("\n")
    textFile.write("Number Of Wins: " + str(set.winsAmount))
    textFile.close()
    endTime = datetime.now()

    print("Seconds: " + str((endTime - startTime).total_seconds()))


run(1000)
