from NormalItem import NormalItem
from tests import sulfuras1, sulfuras2

class Sulfuras(NormalItem):
    
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    def updateQuality(self):
        self.setSellIn(self.sell_in)
        self.setQuality(80)


if __name__ == '__main__':
    # 1
    name = sulfuras1[0][0]
    sellIn = sulfuras1[0][1]
    quality = sulfuras1[0][2]
    item = Sulfuras(name, sellIn, quality)

    for day in sulfuras1:
        assert day == [item.name, item.sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()

    # 2
    name = sulfuras2[0][0]
    sellIn = sulfuras2[0][1]
    quality = sulfuras2[0][2]
    item = Sulfuras(name, sellIn, quality)

    for day in sulfuras2:
        assert day == [item.name, item. sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item. sell_in, item.quality]))
        item.updateQuality()