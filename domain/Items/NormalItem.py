from Item import Item
from tests import dexVest

class NormalItem(Item):
    
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    def reduceSellIn(self   ):
        self.sell_in -= 1
    
    def changeQuality(self):
        qModifier = -1
        if self.sell_in < 0:
            qModifier *= 2
        self.quality += qModifier 

    def checkQualityInRange(self):
        if self.quality <= 0: self.quality = 0
        if self.quality >= 50: self.quality = 50

    def updateQuality(self):
        self.reduceSellIn()
        self.changeQuality()
        self.checkQualityInRange()

    def getName(self):
        return self.name
    def getSellIn(self):
        return self.sell_in
    def getQuality(self):
        return self.quality

    def setName(self, name):
        self.name = name
    def setSellIn(self, sellIn):
        self.sell_in = sellIn
    def setQuality(self, quality):
        self.quality = quality


if __name__ == '__main__':
    name = dexVest[0][0]
    sellIn = dexVest[0][1]
    quality = dexVest[0][2]
    item = NormalItem(name, sellIn, quality)

    for day in dexVest:
        assert day == [item.name, item. sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()