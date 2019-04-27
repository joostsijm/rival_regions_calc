"""Calculate VN regions"""

from rival_regions_calc import Item, DeepExploration, ResourceCoefficient

total_costs = True
gold_price = 0.35
diamond_price = 1600690
regions = {
    '4001': {
        'name': 'Northern Netherlands',
        'resources': {
#            'gold': 379,
#            'oil': 223,
#            'ore': 247,
            'uranium': 2,
#            'diamond': 2,
        },
    },
    '4002': {
        'name': 'Eastern Netherlands',
        'resources': {
#            'gold': 359,
            'oil': 266,
#            'ore': 250,
#            'uranium': 2,
#            'diamond': 2,
        },
    },
    '4003': {
        'name': 'Western Netherlands',
        'resources': {
#            'gold': 372,
#            'oil': 296,
#            'ore': 230,
#            'uranium': 2,
#            'diamond': 2,
        },
    },
    '4004': {
        'name': 'Southern Netherlands',
        'resources': {
#            'gold': 366,
#            'oil': 296,
#            'ore': 211,
#            'uranium': 2,
#            'diamond': 2,
        },
    },
    '4008': {
        'name': 'Amsterdam',
        'resources': {
#            'gold': 418,
#            'oil': 307,
#            'ore': 303,
#            'uranium': 4,
            'diamond': 13,
        },
    },
    '4801': {
        'name': 'Luxembourg',
        'resources': {
#            'gold': 435,
#            'oil': 283,
            'ore': 267,
#            'uranium': 2,
#            'diamond': 2,
        },
    }
}

def calc_regions():
    """Calculate deep exploration"""
    if total_costs:
        print("Resource             cash    old    new  grow %")
    else:
        print("Resource            cash            gold      dia    old    new  grow %")
    for region in regions.values():
        print(region['name'])
        for resource, limit in region['resources'].items():
            resource = Item(resource)
            deep_exploration = DeepExploration(resource, limit)
            deep_exploration.calculate_max()
            old_koef = ResourceCoefficient(resource, limit).calculate() 
            new_koef = ResourceCoefficient(resource, deep_exploration.resource.get_max()).calculate() 
            koef_increase = 100 / old_koef * new_koef - 100
            print_prices(deep_exploration, old_koef, new_koef, koef_increase)


def bucks(integer):
    """Format number"""
    return '{:,}'.format(integer).replace(',', '.')


def print_prices(deep_exploration, old_koef, new_koef, koef_increase):
    """print costs"""
    if total_costs:
        total_cash = round(deep_exploration.gold * gold_price \
            + deep_exploration.diamond * diamond_price \
            + deep_exploration.cash)
        print("%8s %16s %6.2f %6.2f %7.2f" % (
            deep_exploration.resource.name,
            bucks(total_cash),
            old_koef,
            new_koef,
            koef_increase,
        ))
    else:
        print("%8s% 16s% 16s% 9s% 7.2f% 7.2f %7.2f" % (
            deep_exploration.resource.name,
            bucks(deep_exploration.cash),
            bucks(deep_exploration.gold),
            bucks(deep_exploration.diamond),
            old_koef,
            new_koef,
            koef_increase,
        ))


if __name__ == "__main__":
    calc_regions()
