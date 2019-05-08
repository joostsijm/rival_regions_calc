"""ConstructionCosts"""

from . import Building


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
        if not isinstance(building, Building) or not isinstance(current, int):
            raise TypeError
        self.building = building
        self.current = current

    def calculate(self, build_plus):
        """Calculate resources you need based on new buildings"""
        if not isinstance(build_plus, int):
            raise TypeError
        build_total = self.current + build_plus
        building_id = self.building.building_id
        if building_id in (1, 2, 3):
            for i in range(self.current + 1, build_total + 1):
                self.cash += round(pow(i * 300, 1.5))
                self.oil += round(pow(i * 160, 1.5))
                self.ore += round(pow(i * 90, 1.5))
                self.gold += round(pow(i * 2160, 1.5))
                self.diamond += round(pow(i * 0, 1.5))
                self.uranium += round(pow(i * 0, 1))
        elif building_id in (4, 5, 8):
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
