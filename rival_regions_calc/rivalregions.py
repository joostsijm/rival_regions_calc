
"""
The RivalRegions class
"""


class Item():
    """Represents an item in Rival Regions"""

    item_id = None
    name = None

    def __init__(self, item):
        """Initialize Resource"""
        if isinstance(item, str):
            self.name = self.items_inverse.get(item, None)
            if self.name is not None:
                self.item_id = item
        elif isinstance(item, int):
            self.item_id = self.items.get(item, None)
            if self.item_id is not None:
                self.name = item


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


    def print_settings(self):
        """Print the settings"""
        print(
            "Resource:        %16s\n" % (self.resource.name) +
            "user_level:      %16s\n" % (self.user_level) +
            "work_exp:        %16s\n" % (self.work_exp) +
            "factory_level:   %16s\n" % (self.factory_level) +
            "resource_max:    %16s\n" % (self.resource_max) +
            "dep_bonus:       %16s\n" % (self.department_bonus) +
            "nation_bonus:    %16s\n" % (self.nation_bonus) +
            "wage_percentage: %16s\n" % (self.wage_percentage) +
            "state_tax:       %16s\n" % (self.state_tax)
            )


    def calc(self, var, energy=None):
        """Calculate value vased on energy and return"""
        return 10 / energy * var


    def productivity(self, energy=10):
        """Return productivity"""
        return self.calc(self._productivity, energy)


    def withdrawn_points(self, energy=10):
        """Return withdrawn points"""
        return self.calc(self._withdrawn_points, energy)


    def wage(self, energy=10):
        """Return wage"""
        return self.calc(self._wage, energy)


    def tax(self, energy=10):
        """Return tax"""
        return self.calc(self._tax, energy)


    def factory_profit(self, energy=10):
        """Calculate wage"""
        return self.calc(self._factory_profit, energy)


    def resource_koef(self):
        """Calculate coefficient for resource"""
        if self.resource.item_id == 2 or self.resource.item_id == 5:
            return self.resource_max * 0.65
        if self.resource.item_id == 6:
            return self.resource_max * 0.4
        if self.resource.item_id == 11 or self.resource.item_id == 16:
            return self.resource_max * 0.75
        if self.resource.item_id == 21 or self.resource.item_id == 24:
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

        if self.resource.item_id == 6:
            self._productivity = self._productivity * 4
        elif self.resource.item_id == 15:
            self._productivity = self._productivity / 1000
        elif self.resource.item_id == 21:
            self._productivity = self._productivity / 5
        elif self.resource.item_id == 24:
            self._productivity = self._productivity / 1000

        # Tax
        self._tax = self._productivity / 100 * self.state_tax
        self._wage = self._productivity - self._tax

        # Factory profit
        self._factory_profit = self._wage / 100 * (100 - self.wage_percentage)
        self._wage = self._wage - self._factory_profit

        # Withdrawn
        self._withdrawn_points = self._productivity / 40000000


class Building():
    """Represents an item in Rival Regions"""

    building_id = None
    name = None

    def __init__(self, name):
        """Initialize Resource"""
        if not isinstance(name, str):
            raise TypeError
        self.building_id = self.buildings.get(name, None)
        if self.building_id is not None:
            self.name = name


    buildings = {
        "hospital": 1,
        "military base": 2,
        "school": 3,
        "missile system": 4,
        "sea port": 5,
        "power plant": 6,
        "spaceport": 7,
        "airport": 8,
        "house fund": 9,
    }


class ConstructionCosts():
    """Calculate resources needed to raise building levels in region"""

    building = 0
    current = 0

    cash = 0
    oil = 0
    ore = 0
    gold = 0
    uranium = 0
    diamond = 0

    def __init__(self, building, current):
        """Initialize WorkProduction"""
        if not isinstance(building, Building):
            raise TypeError
        if not isinstance(current, int):
            raise TypeError
        self.building = building
        self.current = current


    def calculate(self, build_plus):
        """Calculate resources you need based on new buildings"""
        if not isinstance(build_plus, int):
            raise TypeError
        build_total = self.current + build_plus
        building_id = self.building.building_id  
        if self.building.building_id in (1, 2, 3):
            for i in range(self.current + 1, build_total + 1):
                self.cash += round(pow(i * 300, 1.5))
                self.oil += round(pow(i * 160, 1.5))
                self.ore += round(pow(i * 90, 1.5))
                self.gold += round(pow(i * 2160, 1.5))
                self.diamond += round(pow(i * 0, 1.5))
                self.uranium += round(pow(i * 0, 1))
        elif self.building.building_id in (4, 5, 8):
            for i in range(self.current + 1, build_total + 1):
                self.cash += round(pow(i * 1000, 1.5))
                self.oil += round(pow(i * 10, 1.5))
                self.ore += round(pow(i * 10, 1.5))
                self.gold += round(pow(i * 180, 1.5))
                self.diamond += round(pow(i * 10, 0.7))
                self.uranium += round(pow(i * 0, 1))
        elif self.building.building_id == 6:
            for i in range(self.current + 1, build_total + 1):
                self.cash += round(pow(i * 2000, 1.5))
                self.gold += round(pow(i * 90, 1.5))
                self.oil += round(pow(i * 25, 1.5))
                self.ore += round(pow(i * 25, 1.5))
                self.diamond += round(pow(i * 5, 0.7))
                self.uranium += round(pow(i * 20, 1.5))
        elif self.building.building_id == 7:
            for i in range(self.current + 1, build_total + 1):
                self.cash += round(pow(i * 6000, 1.5))
                self.gold += round(pow(i * 180, 1.5))
                self.oil += round(pow(i * 30, 1.5))
                self.ore += round(pow(i * 25, 1.5))
                self.diamond += round(pow(i * 10, 0.7))
                self.uranium += round(pow(i * 30, 1.5))
        elif self.building.building_id == 9:
            for i in range(self.current + 1, build_total + 1):
                self.cash += round(pow(i * 30, 1.5))
                self.gold += round(pow(i * 216, 1.5))
                self.oil += round(pow(i * 16, 1.5))
                self.ore += round(pow(i * 9, 1.5))
                self.diamond += round(pow(i * 0, 1.5))
                self.uranium += round(pow(i * 0, 1))
