from creature import *


def log_characteristic(creature: Creature, creature_type: str) -> None:
    print('\n',
          'Creature: ' + creature_type + '\n',
          'Position: ' + str(creature.position) + '\n',
          'Stamina : ' + str(creature.stamina) + '\n',
          'Health  : ' + str(creature.health) + '\n',
          'Power   : ' + str(creature.power) + '\n')


def log_predator_runs_out_of_stamina() -> None:
    print('Pray ran into infinity\n')


def log_predator_runs_out_of_health() -> None:
    print('Pray ran into infinity\n')


def log_prey_runs_out_of_health() -> None:
    print('Some R rated things have happened\n')
