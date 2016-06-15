from GamePot import Pot
from Player import Player
from random import randint
from random import shuffle
import itertools

class Board:

    potArray = []
    playerArray = []

    gameStates = [[]]

    storeP1 = 0
    storeP2 = 0
    selectedPlayer = 1
    playNum = 0

    def __init__(self, pots, amountOfPlayers):
        self.potArray = pots
        self.gameStates = self.generateGameStates()
        self.generatePlayers(amountOfPlayers)

    def test(self):
        potIndex = self.askForIndex()
        return self.moveStonesAtIndex(potIndex)



    def generateGameStates(self):
        gameStates = []

        permList = [0, 0, 0, 0, 0, 0]
        for i in range(0, 6):
            comb = self.getPermutations(permList, 6)
            for perm in comb:
                gameStates.append(perm)
            permList[i] = 1
        gameStates.append(permList)
        del gameStates[0]
        gameStates = self.randomizeList(gameStates)
        return gameStates

    def randomizeList(self, inputArray):
        randomKey = range(0, len(inputArray)-1)
        shuffle(randomKey)
        outputArray = range(0, len(inputArray)-1)

        index = 0
        for i in randomKey:
            outputArray[index] = inputArray[i]
            index+=1
        return outputArray


    def getPermutations(self, inputArray, interable):
        perms = list(itertools.permutations(inputArray, interable))
        returnPerms = list()

        for permutation in perms:
            if len(returnPerms) > 0:
                keepPerm = True
                for perm in returnPerms:
                    if perm == permutation:
                        keepPerm = False
                        break
                if keepPerm == True:
                    returnPerms.append(permutation)
            else:
                returnPerms.append(permutation)
        return returnPerms


    def player1Stones(self, index, stoneNum):

        length = len(self.potArray)

        maxIndex1 = (length - (length/2))

        lastPot = (index + stoneNum)
        lastCheck = 0
        i = index + 1
        while i <= lastPot:
            if i == (maxIndex1):
                self.storeP1+=1
                if lastPot == maxIndex1:
                    self.playNum-=1
                    lastCheck = 1
                #lastPot -= 1
                #lastCheck = 1
            if (i) >= length and lastCheck == 0:
                self.potArray[i - length].stoneNum += 1
            elif lastCheck == 0:
                self.potArray[i].stoneNum += 1
                if i == (maxIndex1):
                    lastPot-=1
            lastCheck = 0
            i+=1
        self.potArray[index].stoneNum = 0

    def player2Stones(self, index, stoneNum):

        length = len(self.potArray)

        maxIndex1 = (length / 2)
        maxIndex2 = (length - 1)

        lastPot = (index + stoneNum)
        lastCheck = 0
        i = index + 1
        while i >= index+1 and i < lastPot+1:
            if i == (length):
                self.storeP2 += 1
                if lastPot == length:
                    self.playNum-=1
                    lastCheck = 1
                #lastPot -= 1
                lastCheck = 1
            if i > length:
                self.potArray[i - length - 1].stoneNum += 1
            elif lastCheck == 0:
                self.potArray[i].stoneNum += 1
            lastCheck = 0
            i+=1
        self.potArray[index].stoneNum -=stoneNum

    def setCurrentPlayer(self, index):

        length = len(self.potArray)

        minP1 = 0
        maxP1 = (length - (length/2))

        if index >= minP1 and index <= maxP1:
            self.selectedPlayer = 1
        else:
            self.selectedPlayer = 2


    def moveStonesAtIndex(self, index):
        stone = self.potArray[index]
        self.checkPots()
        if stone.hasStones:
            stoneNum = stone.stoneNum
            self.setCurrentPlayer(index)
            if self.selectedPlayer == 1:
                self.player1Stones(index, stoneNum)
            else:
                self.player2Stones(index, stoneNum)
            self.playNum += 1
            return self.checkGameOver()
        else:
            print "Pot does not contain any stones!"


    def askForIndex(self):
        if self.playNum%2 == 0:
            inputIndex = input("P1 Input Index: ")
            if inputIndex > 5 and inputIndex < 12:
                print "Incorrect Index"
                return self.askForIndex()
            else:
                self.selectedPlayer = 1
                return inputIndex
        else:
            inputIndex = input("P2 Input Index: ")
            if inputIndex < 6 and inputIndex >= 0:
                print "Incorrect Index"
                return self.askForIndex()
            else:
                self.selectedPlayer = 2
                return inputIndex





    def checkPots(self):
        for pot in self.potArray:
            if pot.stoneNum <= 0:
                pot.hasStones = False
            else:
                pot.hasStones = True

    def checkGameOver(self):
        self.checkPots()
        if not self.potArray[0].hasStones and not self.potArray[1].hasStones and not self.potArray[2].hasStones and not self.potArray[3].hasStones and not self.potArray[4].hasStones and not self.potArray[5].hasStones:
            return 1
        if not self.potArray[11].hasStones and not self.potArray[10].hasStones and not self.potArray[9].hasStones and not \
        self.potArray[8].hasStones and not self.potArray[7].hasStones and not self.potArray[6].hasStones:
            return 1
        return 0



    def printValues(self):
        print "Store1 " + str(self.storeP1)
        print "Store2 " + str(self.storeP2)
        index = 0
        for i in self.potArray:
            print "Pot" + str(index)
            print i.stoneNum
            index += 1

    def generatePlayers(self, playerAmount):
        for i in range(0, playerAmount):
            player = Player(self.generateMoveSet())
            self.playerArray.append(player)

    def generateMoveSet(self):
        moveSet = []
        for state in self.gameStates:
            movesArray = []
            for i in range(0, len(state)):
                if state[i] == 1:
                    movesArray.append(i)
            if len(movesArray) > 1:
                rand = randint(0, len(movesArray)-1)
                move = movesArray[rand]
                moveSet.append(move)
            else:
                move = movesArray[0]
                moveSet.append(move)
        return moveSet