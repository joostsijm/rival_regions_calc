
"""
Test file
"""

from rival_regions_calc import Item, WorkProduction

gold = Item("gold")

wp = WorkProduction(gold)

wp.user_level = 83
wp.work_exp = 120981
wp.factory_level = 141
wp.resource_max = 379
wp.nation_bonus = True
wp.department_bonus = 34
wp.wage_percentage = 99
wp.state_tax = 20

wp.calculate()

print("----")
print("Productivity :  %10d" % wp.productivity())
print("State Tax    : -%10d" % wp.tax())
print("Factory Prof : -%10d" % wp.factory_profit())
print("Wage         :  %10d" % wp.wage())
print("Withdrawn    :  %10.2f" % wp.withdrawn_points())
