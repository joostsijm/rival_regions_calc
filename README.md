# Rival Regions Calc
  
Unofficial calculator for Rival Regions. Easily calculate common known formulas from the game.

## Currently supported
* Work productivity

## Install

```bash
$ pip install rival-regions-calc

```

## Demo
### Production

```python
from rival_regions_calc import Item, WorkProduction

RESOURCE = Item("oil")
WP = WorkProduction(RESOURCE)

WP.user_level = 86
WP.work_exp = 142000
WP.factory_level = 185
WP.resource_max = 371
WP.department_bonus = 1.9
WP.wage_percentage = 100
WP.tax_rate = 2
WP.profit_share = 75

WP.calculate()

print(WP.wage())
```

### Construction

```python
from rival_regions_calc import ConstructionCosts, Building

BUILDING = Building("hospital")
CC = ConstructionCosts(BUILDING, 1805)

CC.calculate(50)

print(CC.cash)
print(CC.gold)
print(CC.oil)
print(CC.ore)
```

### Deep exploration

```python
from rival_regions_calc import Item, DeepExploration

resource = Item("oil")
DE = DeepExploration(resource, 223)

DE.calculate_max()

print(DE.cash)
print(DE.gold)
print(DE.diamond)
```

### Resource coefficient

```python
from rival_regions_calc import ResourceCoefficient, Item

resource = Item("oil")
RC = ResourceCoefficient(resource, 266)
print(RC.calculate())
RC = ResourceCoefficient(resource, 371)
print(RC.calculate())
```

## Development

I'll add formulas if I think they are important. 
If you'd like to see a more improvements you can open an issue or make pull request.
