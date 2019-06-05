
"""
Test file
"""

from rival_regions_calc import Item, WorkProduction

RESOURCE = Item("oil")
WP = WorkProduction(RESOURCE)

WP.user_level = 86
WP.work_exp = 142000
WP.factory_level = 185
WP.resource_max = 371
WP.nation_bonus = True
WP.department_bonus = 1.9
WP.wage_percentage = 100
WP.state_tax = 2

WP.calculate()

WP.print_settings()
ENERGY = 10
print("----")
print("Productivity :  {:17,.0f}".format(WP.productivity(ENERGY)))
print("State Tax    : -{:17,.0f}".format(WP.tax(ENERGY)))
print("Factory Prof : -{:17,.0f}".format(WP.factory_profit(ENERGY)))
print("Wage         :  {:17,.0f}".format(WP.wage(ENERGY)))
print("Withdrawn    :  {:17,.2f}".format(WP.withdrawn_points(ENERGY)))
