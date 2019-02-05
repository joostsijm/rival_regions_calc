# Rival Regions Calc
  
Unofficial calculator for Rival Regions. Easily calculate common known formulas from the game.

## Currently supported
* Work productivity

## Install
(Not on pypi.org yet)

```bash
$ pip install rival-regions-calc

```

## Simple Demo

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

## Documentation

Other information about functions and exceptions can be found on the [wiki.](https://github.com/joostsijm/rival_regions_calc/wiki)

## Development

I'll add formulas if I think they are important. 
If you'd like to see a more improvement you can open an issue or make pull request.
