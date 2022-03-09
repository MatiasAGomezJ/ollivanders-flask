from NormalItem import NormalItem
from tests import agedBrie

class AgedBrie(NormalItem):
    
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    def changeQuality(self):
        qModifier = 1
        if self.sell_in < 0:
            qModifier *= 2
        self.quality += qModifier 


if __name__ == '__main__':
    name = agedBrie[0][0]
    sellIn = agedBrie[0][1]
    quality = agedBrie[0][2]
    item = AgedBrie(name, sellIn, quality)

    for day in agedBrie:
        assert day == [item.name, item. sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()