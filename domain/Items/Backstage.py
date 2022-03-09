from NormalItem import NormalItem
from tests import backstage1, backstage2, backstage3

class Backstage(NormalItem):
    
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    def changeQuality(self):
        qModifier = 1

        if self.sell_in < 5:
            qModifier *= 3
        elif self.sell_in < 10:
            qModifier *= 2
        self.quality += qModifier 

        if self.sell_in < 0:
            self.setQuality(0)


if __name__ == '__main__':
    # 1
    name = backstage1[0][0]
    sellIn = backstage1[0][1]
    quality = backstage1[0][2]
    item = Backstage(name, sellIn, quality)

    for day in backstage1:
        assert day == [item.name, item. sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()

    # 2
    name = backstage2[0][0]
    sellIn = backstage2[0][1]
    quality = backstage2[0][2]
    item = Backstage(name, sellIn, quality)

    for day in backstage2:
        assert day == [item.name, item. sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()

    # 3
    name = backstage3[0][0]
    sellIn = backstage3[0][1]
    quality = backstage3[0][2]
    item = Backstage(name, sellIn, quality)

    for day in backstage3:
        assert day == [item.name, item. sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()