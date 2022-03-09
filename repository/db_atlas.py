from repository.stock import stock


class db_atlas:
    @staticmethod
    def get_stock():
        return stock

    @staticmethod
    def get_item(name, quality, sell_in):
        items = []
        for item in db_atlas.get_stock():
            if item.get("name").lower() == name.lower() and item.get("quality") == quality and item.get("sell_in") == sell_in:
                items.append(item)
        return items

    @staticmethod
    def get_name(name):
        items = []
        for item in db_atlas.get_stock():
            if item.get("name").lower() == name.lower():
                items.append(item)
        return items
