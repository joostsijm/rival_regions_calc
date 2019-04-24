"""Test file for deep exploration"""

from rival_regions_calc import Item, DeepExploration

resource = Item("oil")
DE = DeepExploration(resource, 223)

DE.calculate_max()

def bucks(integer):
    """Format number"""
    return '{:,}'.format(integer).replace(',', '.')

print('%17s $' % bucks(DE.cash))
print('%17s G' % bucks(DE.gold))
print('%17s pcs.' % bucks(DE.diamond))
