"""DeepExploration"""

import math
from . import Item


class DeepExploration():
    """Calculate deep exploration, costs and improved production"""

    base = 0
    resource = None

    cash = 0
    gold = 0
    diamond = 0

    resource_types = {
        2: 4,
        5: 2,
        6: 4,
        11: 40,
        15: 70,
    }

    resource_max = {
        2: 371,
        5: 356,
        6: 637,
        11: 25,
        15: 27,
    }

    def __init__(self, resource, base):
        """Initialize WorkProduction"""
        if not isinstance(resource, Item) or not isinstance(base, int):
            raise TypeError
        self.resource = resource
        self.base = base

    def calculate(self, deep_exploration):
        """Calculate exploration costs"""
        if not isinstance(deep_exploration, int):
            raise TypeError
        for i in range(1, deep_exploration + 1):
            tmp = math.ceil(
                self.resource_types[self.resource.item_id] *
                (self.base + i) * 50000
            )

            self.cash = self.cash + math.ceil(tmp * 0.95)
            self.gold = self.gold + math.ceil(tmp * 2)
            self.diamond = self.diamond + math.ceil(tmp * 1.0E-5)

    def calculate_max(self):
        """calculate costs for max deep exploration"""
        max_exploration = self.resource_max[self.resource.item_id] - self.base
        self.calculate(max_exploration)
