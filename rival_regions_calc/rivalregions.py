
"""
The RivalRegions class
"""


class Item():
    """Represents an item in Rival Regions"""

    id = None
    name = None

    def __init__(self, name):
        """Initialize Resource """
        self.id = self.items.get(name, None)
        if self.name is not None:
            self.name = name


    items = {
        "oil": 2,
        "ore": 5,
        "gold": 6,
        "uranium": 11,
        "diamond": 15,
        "liquid oxygen": 21,
        "helium": 24,
    }


class WorkProduction():
    """Calculate work productivity based on parameters

    Sources:
    http://wiki.rivalregions.com/Work_formulas
    """

    # Input
    resource = None
    user_level = 0
    work_exp = 0
    factory_level = 0
    resource_max = 0
    department_bonus = 0
    nation_bonus = False

    # Calculated
    _withdrawn_points = 0
    _productivity = 0

    def withdrawn_points(self):
        """Check if withdrawn points are calculated"""
        if self._withdrawn_points == 0:
            self.calculate()
        return self._withdrawn_points


    def productivity(self):
        """Check if productivity is calculated"""
        if self._productivity == 0:
            self.calculate()
        return self._productivity


    def resource_koef(self):
        """Calculate coefficient for resource"""
        if self.resource.id == 2 or self.resource.id == 5:
            return self.resource_max * 0.65
        if self.resource.id == 6:
            return self.resource_max * 0.4
        if self.resource.id == 11 or self.resource.id == 16:
            return self.resource_max * 0.75
        if self.resource.id == 21 or self.resource.id == 24:
            return pow(self.resource_max * 2, 0.4)
        return 0


    def calculate(self, energy=10):
        """Return productivity """
        if energy%10 > 0:
            raise Exception

        self._productivity = 20 * \
                pow(self.user_level, 0.8) * \
                pow(self.resource_koef() / 10, 0.8) * \
                pow(self.factory_level, 0.8) * \
                pow(self.work_exp / 10, 0.6)

        if self.nation_bonus:
            self._productivity = self._productivity * 1.2

        self._productivity = self._productivity * (1 + self.department_bonus / 100)
        self._productivity = energy / 10 * self._productivity
        self._withdrawn_points = self._productivity / 40000000
