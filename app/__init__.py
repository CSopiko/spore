from typing import Tuple
from log import *
from creature import Creature, Predator, Prey

SIMULATION_NUM = 100


def main() -> None:
    for _ in range(SIMULATION_NUM):
        log_start_simulation()
        predator, prey = evolve_creatures()
        if chase(predator, prey):
            combat(predator, prey)


def evolve_creatures() -> Tuple[Creature, Creature]:
    prey = Prey()
    predator = Predator(prey.position)
    log_characteristic(predator, 'Predator')
    log_characteristic(prey, 'Prey')
    return predator, prey


def chase(predator: Creature, prey: Creature) -> bool:
    """
    :param predator: Creature chases something to eat
    :param prey: Creature that's wanted to be eaten
    :return: whether or not Creatures enter the combat
    """
    while True:
        if predator.get_position() >= prey.get_position():
            return True
        if predator.get_stamina() <= 0:
            log_predator_runs_out_of_stamina()
            return False
        predator.movement()
        prey.movement()
        # log_characteristic(predator, 'Predator')
        # log_characteristic(prey, 'Prey')


def combat(predator: Creature, prey: Creature) -> None:
    while True:
        if predator.get_health() <= 0:
            log_predator_runs_out_of_health()
            return
        if prey.get_health() <= 0:
            log_prey_runs_out_of_health()
            return
        prey.health += predator.attack()
        predator.health += prey.attack()


if __name__ == '__main__':
    main()
