class GildedRose(object):
    def __init__(self, items):
        self.stock = items

    def updateQuality(self):
        for item in self.stock:
            item.updateQuality()

    def addItem(self, newItem):
        self.stock.append(newItem)

    def getStock(self):
        return self.stock
