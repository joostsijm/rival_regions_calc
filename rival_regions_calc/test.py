
"""
Test file
"""

from rivalregions import Item, WorkProduction

gold = Item("gold")

wp = WorkProduction(gold)

wp.user_level = 83
wp.work_exp = 120850
wp.factory_level = 141
wp.resource_max = 379
wp.nation_bonus = True
wp.department_bonus = 34
wp.wage_percentage = 99
wp.tax = 20

wp.calculate()

energy = 10
print("Productivity : %s" % wp.productivity(energy=energy))
print("Wage         : %s" % wp.wage(energy=energy))
print("Withdrawn    : %s" % wp.withdrawn_points(energy))
