# Rival Regions Calc
  
Unofficial calculator for Rival Regions. Easily calculate common known formulas from the game.

## Currently supported
* Work productivity

## Install
(Not on pypi.org yet)

```bash
$ pip install rival-regions-calc

```

## Demo
### Production

```python
from rival_regions_calc import Item, WorkProduction

gold = Item("gold")
wp = WorkProduction(gold)

wp.user_level = 80
wp.work_exp = 120981
wp.factory_level = 140
wp.resource_max = 359
wp.nation_bonus = True
wp.department_bonus = 28
wp.wage_percentage = 99
wp.state_tax = 15

wp.calculate()

print(wp.productivity())
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

## Documentation

Other information about functions and exceptions can be found on the [wiki.](https://github.com/joostsijm/rival_regions_calc/wiki)

## Development

I'll add formulas if I think they are important. 
If you'd like to see a more improvements you can open an issue or make pull request.
