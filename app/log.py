from creature import *


def log_characteristic(creature: Creature, creature_type: str) -> None:
    print('\n',
          'Creature: ' + creature_type + '\n',
          'Position: ' + str(creature.position) + '\n',
          'Stamina : ' + str(creature.stamina) + '\n',
          'Health  : ' + str(creature.health) + '\n',
          'Power   : ' + str(creature.power) + '\n',
          'Legs    : ' + str(creature.legs) + '\n',
          'Wings   : ' + str(creature.wings) + '\n',
          'Claws   : ' + str(creature.claws_type) + '\n',
          'Teeth   : ' + str(creature.teeth_type))


def log_predator_runs_out_of_stamina() -> None:
    print('Pray ran into infinity')


def log_predator_runs_out_of_health() -> None:
    print('Pray ran into infinity')


def log_prey_runs_out_of_health() -> None:
    print('Some R rated things have happened')


def log_combat_starts() -> None:
    print('Combat starts now')


def log_start_simulation() -> None:
    print('*****************START*****************')
