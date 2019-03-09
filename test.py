
"""
Test file
"""

from rival_regions_calc import Item, WorkProduction

resource = Item("oil")
wp = WorkProduction(resource)

wp.user_level = 67
wp.work_exp = 87063
wp.factory_level = 123
wp.resource_max = 379
wp.nation_bonus = True
wp.department_bonus = 19
wp.wage_percentage = 100
wp.state_tax = 20

wp.calculate()

wp.print_settings()
energy=1.9
print("----")
print("Productivity :  {:17,.0f}".format(wp.productivity(energy)))
print("State Tax    : -{:17,.0f}".format(wp.tax(energy)))
print("Factory Prof : -{:17,.0f}".format(wp.factory_profit(energy)))
print("Wage         :  {:17,.0f}".format(wp.wage(energy)))
print("Withdrawn    :  {:17,.2f}".format(wp.withdrawn_points(energy)))
