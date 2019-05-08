"""Item"""


class Item():
    """Represents an item in Rival Regions"""

    item_id = None
    name = None

    def __init__(self, item):
        """Initialize Resource"""
        if isinstance(item, str):
            self.item_id = self.items[item]
            self.name = item
        elif isinstance(item, int):
            self.name = self.items_inverse[item]
            self.item_id = item

    items = {
        "cash": 0,
        "oil": 2,
        "ore": 5,
        "gold": 6,
        "uranium": 11,
        "diamond": 15,
        "liquid oxygen": 21,
        "helium": 24,
    }

    items_inverse = {
        0: "cash",
        2: "oil",
        5: "ore",
        6: "gold",
        11: "uranium",
        15: "diamond",
        21: "liquid oxygen",
        24: "helium",
    }

    resource_max = {
        2: 371,
        5: 356,
        6: 637,
        11: 25,
        15: 27,
    }

    def get_max(self):
        """return max for resource"""
        return self.resource_max[self.item_id]
