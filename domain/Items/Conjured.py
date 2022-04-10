from NormalItem import NormalItem
from tests import manaCake


class Conjured(NormalItem):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    # def changeQuality(self):
    #     qModifier = -2
    #     if self.sell_in < 0:
    #         qModifier *= 2
    #     self.quality += qModifier


if __name__ == "__main__":
    name = manaCake[0][0]
    sellIn = manaCake[0][1]
    quality = manaCake[0][2]
    item = Conjured(name, sellIn, quality)

    for day in manaCake:
        assert day == [item.name, item.sell_in, item.quality]
        print(str(day) + " == " + str([item.name, item.sell_in, item.quality]))
        item.updateQuality()
