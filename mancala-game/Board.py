class Board:
    potArray = []
    storeP1 = 0
    storeP2 = 0
    selectedPlayer = 1
    playNum = 0

    def __init__(self, pots):
        self.potArray = pots

    def test(self):
        potIndex = self.askForIndex()
        return self.moveStonesAtIndex(potIndex)

    def player1Stones(self, index, stoneNum):

        length = len(self.potArray)

        maxIndex1 = (length - (length / 2))

        lastPot = (index + stoneNum)
        lastCheck = 0
        i = index + 1
        while i <= lastPot:
            if i == maxIndex1:
                self.storeP1 += 1
                if lastPot == maxIndex1:
                    self.playNum -= 1
                    lastCheck = 1
                    # lastPot -= 1
                    # lastCheck = 1
            if i >= length and lastCheck == 0:
                self.potArray[i - length].stoneNum += 1
            elif lastCheck == 0:
                self.potArray[i].stoneNum += 1
                if i == maxIndex1:
                    lastPot -= 1
            lastCheck = 0
            i += 1
        self.potArray[index].stoneNum = 0

    def player2Stones(self, index, stoneNum):

        length = len(self.potArray)

        lastPot = (index + stoneNum)
        lastCheck = 0
        i = index + 1
        while index + 1 <= i < lastPot + 1:
            if i == length:
                self.storeP2 += 1
                if lastPot == length:
                    self.playNum -= 1
                # lastPot -= 1
                lastCheck = 1
            if i > length:
                self.potArray[i - length - 1].stoneNum += 1
            elif lastCheck == 0:
                self.potArray[i].stoneNum += 1
            lastCheck = 0
            i += 1
        self.potArray[index].stoneNum -= stoneNum

    def setCurrentPlayer(self):

        if self.playNum % 2 == 0:
            self.selectedPlayer = 1
        else:
            self.selectedPlayer = 2

    def moveStonesAtIndex(self, index):
        stone = self.potArray[index]
        self.checkPots()
        self.setCurrentPlayer()
        if stone.hasStones:
            stoneNum = stone.stoneNum
            self.setCurrentPlayer()
            if self.selectedPlayer == 1:
                self.player1Stones(index, stoneNum)
            else:
                self.player2Stones(index, stoneNum)
            self.playNum += 1
            return self.checkGameOver()
        else:
            print "Pot does not contain any stones!"

    def askForIndex(self):
        if self.playNum % 2 == 0:
            inputIndex = input("P1 Input Index: ")
            if 5 < inputIndex < 12:
                print "Incorrect Index"
                return self.askForIndex()
            else:
                self.selectedPlayer = 1
                return inputIndex
        else:
            inputIndex = input("P2 Input Index: ")
            if 6 > inputIndex >= 0:
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
        if not self.potArray[0].hasStones and not self.potArray[1].hasStones and not self.potArray[2].hasStones and not \
                self.potArray[3].hasStones and not self.potArray[4].hasStones and not self.potArray[5].hasStones:
            return 1
        if not self.potArray[11].hasStones and not self.potArray[10].hasStones and not self.potArray[
            9].hasStones and not \
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
