"""WorkProduction"""

from . import Item
from . import ResourceCoefficient


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
    tax_rate = 0
    profit_share = 0

    # Calculated
    _withdrawn_points = 0
    _productivity = 0
    _wage = 0
    _tax = 0
    _factory_profit = 0

    def __init__(self, item=None):
        """Initialize WorkProduction"""
        if isinstance(item, Item) or item is None:
            self.resource = item
        else:
            raise TypeError

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
            "tax_rate:        %16s\n" % (self.tax_rate)
            )

    def productivity(self, energy=10):
        """Return productivity"""
        return self._productivity * energy / 10

    def withdrawn_points(self, energy=10):
        """Return withdrawn points"""
        return self._withdrawn_points * energy / 10

    def wage(self, energy=10):
        """Return wage"""
        return self._wage * energy / 10

    def tax(self, energy=10):
        """Return tax"""
        return self._tax * energy / 10

    def state_tax(self, energy=10):
        """Return state tax"""
        return self._tax / 100 * (100 - self.profit_share) * energy / 10

    def autonomy_tax(self, energy=10):
        """Return state tax"""
        return self._tax / 100 * self.profit_share * energy / 10

    def factory_profit(self, energy=10):
        """Calculate wage"""
        return self._factory_profit * energy / 10

    def additional_koef(self):
        """Calculcate the additional koef"""
        if self.resource.item_id == 6:
            self._productivity = self._productivity * 4
        elif self.resource.item_id == 15:
            self._productivity = self._productivity / 1000
        elif self.resource.item_id == 21:
            self._productivity = self._productivity / 5
        elif self.resource.item_id == 24:
            self._productivity = self._productivity / 1000

    def calculate(self):
        """Calculate productivity"""
        self._productivity = 0.2 * \
            pow(self.user_level, 0.8) * \
            ResourceCoefficient(
                self.resource,
                self.resource_max
            ).calculate() * \
            pow(self.factory_level, 0.8) * \
            pow(self.work_exp / 10, 0.6)

        if self.nation_bonus:
            self._productivity = self._productivity * 1.2

        self._productivity = \
            self._productivity * (1 + self.department_bonus / 100)

        self.additional_koef()

        # Tax
        self._tax = self._productivity / 100 * self.tax_rate
        self._wage = self._productivity - self._tax

        # Factory profit
        self._factory_profit = self._wage / 100 * (100 - self.wage_percentage)
        self._wage = self._wage - self._factory_profit

        # Withdrawn
        self._withdrawn_points = self._productivity / 40000000
