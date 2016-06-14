from Pot import Pot

class Board:

    potArray = []
    storeP1 = 0
    storeP2 = 0
    currentPlayer = 1

    def __init__(self, pots):
        self.potArray = pots

    def test(self):
        potIndex = self.askForIndex()
        self.moveStonesAtIndex(potIndex)








    def player1Stones(self, index, stoneNum):

        length = len(self.potArray)

        maxIndex1 = (length - (length/2))

        lastPot = (index + stoneNum)

        if index <= maxIndex1 and lastPot >= maxIndex1:
            for i in range(index+1, lastPot+1, 1):
                if i == (maxIndex1):
                    self.storeP1+=1
                    #TODO implement turn rule
                if (i-1) >= length:
                    self.potArray[(i-1) - length].stoneNum += 1
                else:
                    self.potArray[i-1].stoneNum += 1

            self.potArray[index].stoneNum = 0
            self.checkPots()


    def player2Stones(self, index, stoneNum):

        length = len(self.potArray)

        maxIndex1 = (length / 2)
        maxIndex2 = (length - 1)

        if index >= maxIndex1 and (index + stoneNum) >= length:
            for i in range(index + 1, (index + stoneNum)+1, 1):
                if i == (length):
                    self.storeP2 += 1
                    # TODO implement turn rule
                if i >= length:
                    self.potArray[i-length].stoneNum += 1
                else:
                    self.potArray[i].stoneNum += 1

            self.potArray[index].stoneNum = 0
            self.checkPots()

    def setCurrentPlayer(self, index):

        length = len(self.potArray)

        minP1 = 0
        maxP1 = (length - (length/2))

        if index >= minP1 and index <= maxP1:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 2


    def moveStonesAtIndex(self, index):
        stone = self.potArray[index]
        if stone.hasStones:
            stoneNum = stone.stoneNum
            self.setCurrentPlayer(index)
            self.player1Stones(index, stoneNum)
            self.player2Stones(index, stoneNum)
            #self.printValues()
        else:
            print "Pot does not contain any stones!"



    def askForIndex(self):
        inputIndex = input("Input Index: ")
        return inputIndex

    def checkPots(self):
        for pot in self.potArray:
            if pot.stoneNum <= 0:
                pot.hasStones = False
            else:
                pot.hasStones = True

    def checkGameOver(self):
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