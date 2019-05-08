"""ResourceCoefficient"""

from . import Item


class ResourceCoefficient():
    """Calculate resource coefficient in working formula"""

    resource = None
    limit = 0

    def calculate(self):
        """Calculate the coefficient"""
        return pow(self.limit * self.resource_koef() / 10, 0.8)

    def __init__(self, resource, limit):
        """Initialize ResourceCoefficient"""
        if not isinstance(resource, Item) or not isinstance(limit, int):
            raise TypeError
        self.resource = resource
        self.limit = limit

    def resource_koef(self):
        """Calculate coefficient for resource"""
        if self.resource.item_id == 2 or self.resource.item_id == 5:
            return 0.65
        if self.resource.item_id == 6:
            return 0.4
        if self.resource.item_id == 11 or self.resource.item_id == 15:
            return 0.75
        if self.resource.item_id == 21 or self.resource.item_id == 24:
            return 0.4
        return 0
