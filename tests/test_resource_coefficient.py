"""Test file for resource coefficient"""

from rival_regions_calc import ResourceCoefficient, Item

resource = Item("oil")
RC = ResourceCoefficient(resource, 266)
print(RC.calculate())
RC = ResourceCoefficient(resource, 371)
print(RC.calculate())
