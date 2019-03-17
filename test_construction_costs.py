"""Test file for construction costs"""

from rival_regions_calc import ConstructionCosts, Building


BUILDING = Building("Hospital")
CC = ConstructionCosts(BUILDING, 1805)

CC.calculate(50)

def bucks(integer):
    """Format number"""
    return '{:,}'.format(integer).replace(',', '.')

print('%17s $' % bucks(CC.cash))
print('%17s G' % bucks(CC.gold))
print('%17s bbl' % bucks(CC.oil))
print('%17s kg' % bucks(CC.ore))
print('%17s pcs.' % bucks(CC.diamond))
print('%17s g' % bucks(CC.uranium))
