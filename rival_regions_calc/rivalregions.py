
"""
The RivalRegions class
"""


class Item():
    """Represents an item in Rival Regions"""

    id = None
    name = None

    def __init__(self, name):
        """Initialize Resource"""
        self.id = self.items.get(name, None)
        if self.id is not None:
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
    wage_percentage = 100
    state_tax = 0

    # Calculated
    _withdrawn_points = 0
    _productivity = 0
    _wage = 0
    _tax = 0
    _factory_profit = 0


    def __init__(self, item):
        """Initialize WorkProduction"""
        if not isinstance(item, Item):
            raise TypeError
        self.resource = item


    def calc(self, var, energy=None, gold=None):
        """Calculate value vased on energy and return"""
        if var == 0:
            self.calculate()
        if gold is not None:
            if gold % 1 > 0:
                raise Exception
            energy = gold * 10
        if energy % 10 > 0:
            raise Exception
        return round(energy / 10 * var)


    def productivity(self, energy=10, gold=None):
        """Return productivity"""
        return self.calc(self._productivity, energy, gold)


    def withdrawn_points(self, energy=10, gold=None):
        """Return withdrawn points"""
        return self.calc(self._withdrawn_points, energy, gold)


    def wage(self, energy=10, gold=None):
        """Return wage"""
        return self.calc(self._wage, energy, gold)


    def tax(self, energy=10, gold=None):
        """Return tax"""
        return self.calc(self._tax, energy, gold)


    def factory_profit(self, energy=10, gold=None):
        """Calculate wage"""
        if self._factory_profit == 0:
            self.calculate()
        if gold is not None:
            if gold % 1 > 0:
                raise Exception
            energy = gold * 10
        if energy % 10 > 0:
            raise Exception
        return round(energy / 10 * self._factory_profit)


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


    def calculate(self):
        """Calculate productivity"""

        self._productivity = 20 * \
                pow(self.user_level, 0.8) * \
                pow(self.resource_koef() / 10, 0.8) * \
                pow(self.factory_level, 0.8) * \
                pow(self.work_exp / 10, 0.6)

        if self.nation_bonus:
            self._productivity = self._productivity * 1.2

        self._productivity = self._productivity * (1 + self.department_bonus / 100)

        # Tax
        self._tax = self._productivity / 100 * self.state_tax
        self._wage = self._productivity - self._tax

        # Factory profit
        self._factory_profit = self._wage / 100 * (100 - self.wage_percentage)
        self._wage = self._wage - self._factory_profit

        # Withdrawn
        self._withdrawn_points = self._productivity / 40000000
