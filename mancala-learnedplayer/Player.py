class Player:
    stateMoveDictionary = {}
    winsAmount = 0

    def __init__(self):
        self.winsAmount = 0
        self.stateMoveDictionary = {}

    def reInitDict(self):
        newDict = {}
        for i in range(0, len(self.stateMoveDictionary)):
            currentKey = self.stateMoveDictionary.keys()[i]
            newDict[currentKey] = self.stateMoveDictionary[currentKey]
        self.stateMoveDictionary = newDict
