"""Building"""


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
