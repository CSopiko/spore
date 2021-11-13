from typing import Tuple
from log import *
from creature import Creature, Predator, Prey

SIMULATION_NUM = 1


def main() -> None:
    for _ in range(SIMULATION_NUM):
        predator, prey = evolve_creatures()
        log_characteristic(predator, 'Predator')
        log_characteristic(prey, 'Prey')
        chase(predator, prey)
        combat(predator, prey)


def evolve_creatures() -> Tuple[Creature, Creature]:
    prey = Prey()
    predator = Predator()
    return predator, prey


def chase(predator, prey) -> None:
    pass


def combat(predator, prey):
    pass


if __name__ == '__main__':
    main()
