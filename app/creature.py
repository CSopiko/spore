from random import randint, sample
from typing import Any

from attack import *
from movement import *
from dataclasses import dataclass

LEGS = 'legs'
WINGS = 'wings'
NO_LIMB = 'no_limb'

CLAWS = 'claws'
SMALL = 'small'
MEDIUM = 'medium'
BIG = 'big'
NO_CLAW = 'no_claw'
CLAWS_TYPES = {SMALL: 0, MEDIUM: 1, BIG: 2, NO_CLAW: 3}

TEETH = 'teeth'
BLUNT = 'blunt'
SHARP = 'sharp'
NO_TEETH = 'no_teeth'
SUPER_SHARP = 'super_sharp'
TEETH_TYPES = {BLUNT: 0, SHARP: 1, SUPER_SHARP: 2, NO_TEETH: 3}

# LIMBS = {LEGS: 0, WINGS: 1,  CLAWS: 2, TEETH: 3}
LIMBS = {0: LEGS, 1: WINGS, 2: CLAWS, 3: TEETH}

# Ranges:
POWER_RANGE = [1, 3]
POSITION_RANGE = [0, 100]
HEALTH_RANGE = [50, 100]
STAMINA_RANGE = [50, 100]

LEG_NUM_RANGE = [0, 2]
WING_NUM_RANGE = [0, 2]

# {limb_type: {minimum_amount: [types of movement]}}
MOVEMENTS = {LEGS: {1: [HoppingMovement], 2: [WalkingMovement, RunningMovement]},
             WINGS: {2: [FlyingMovement]}, NO_LIMB: {0: [CrawlingMovement]}}

# {limb_type: {type: [types of attack]}}
ATTACKS = {CLAWS: {CLAWS_TYPES[SMALL]: [SmallClawsAttack],
                   CLAWS_TYPES[MEDIUM]: [MediumClawsAttack],
                   CLAWS_TYPES[BIG]: [BigClawsAttack],
                   CLAWS_TYPES[NO_CLAW]: [DefaultAttack]},
           TEETH: {TEETH_TYPES[BLUNT]: [BluntTeethAttack],
                   TEETH_TYPES[SHARP]: [SharpTeethAttack],
                   TEETH_TYPES[SUPER_SHARP]: [SuperSharpTeethAttack],
                   TEETH_TYPES[NO_TEETH]: [DefaultAttack]}}


def generate_characteristics(min_position: int = POSITION_RANGE[0],
                             max_position: int = POSITION_RANGE[1]) -> tuple[int, int, int, int, int, int, Any, Any]:
    position = randint(min_position, max_position)
    power = randint(POWER_RANGE[0], POWER_RANGE[1])
    health = randint(HEALTH_RANGE[0], HEALTH_RANGE[1])
    stamina = randint(STAMINA_RANGE[0], STAMINA_RANGE[1])

    legs = randint(LEG_NUM_RANGE[0], LEG_NUM_RANGE[1])
    wings = randint(WING_NUM_RANGE[0], WING_NUM_RANGE[1])
    claws_type = {v: k for k, v in CLAWS_TYPES.items()}[randint(0, len(CLAWS_TYPES) - 1)]
    teeth_type = {v: k for k, v in TEETH_TYPES.items()}[randint(0, len(TEETH_TYPES) - 1)]

    return position, power, health, stamina, legs, wings, claws_type, teeth_type


@dataclass
class Creature:
    # position: int
    # power: int = 1
    # health: int = 100
    # stamina: int = 100

    def __init__(self, position: int = 0, power: int = 1, health: int = 100, stamina: int = 100,
                 legs: int = 0, wings: int = 0, claws_type: str = NO_CLAW,
                 teeth_type: str = NO_TEETH):
        self.position = position
        self.power = power
        self.health = health
        self.stamina = stamina

        self.legs = legs
        self.wings = wings
        self.claws_type = claws_type
        self.teeth_type = teeth_type

    def movement(self) -> None:
        leg = [k for k in MOVEMENTS[LEGS] if self.legs >= k] + [-1]
        wing = [k for k in MOVEMENTS[WINGS] if self.wings >= k] + [-1]
        max_legs = max(leg)
        max_wings = max(wing)
        if max_legs != -1:
            movement_class = MOVEMENTS[LEGS][max_legs][0]()
        elif max_wings != -1:
            movement_class = MOVEMENTS[WINGS][max_wings][0]()
        else:
            movement_class = MOVEMENTS[NO_LIMB][0][0]()
        stamina, position = movement_class.move()
        self.stamina += stamina
        self.position += position

    def attack(self) -> int:
        claw = [c for c in ATTACKS[CLAWS] if c == CLAWS_TYPES[self.claws_type]]
        tooth = [t for t in ATTACKS[TEETH] if t == TEETH_TYPES[self.teeth_type]]

        if claw == NO_CLAW and tooth == NO_TEETH:
            damage = ATTACKS[TEETH][TEETH_TYPES[NO_TEETH]][0]().attack(self.power)
        elif claw == NO_CLAW:
            damage = ATTACKS[TEETH][TEETH_TYPES[self.teeth_type]][0]().attack(self.power)
        elif tooth == NO_TEETH:
            damage = ATTACKS[CLAWS][CLAWS_TYPES[self.claws_type]][0]().attack(self.power)
        else:
            damage = ATTACKS[CLAWS][CLAWS_TYPES[self.claws_type]][0]().attack(self.power) \
                     + ATTACKS[TEETH][TEETH_TYPES[self.teeth_type]][0]().attack(self.power)
        return damage

    def get_position(self) -> int:
        return self.position

    def get_health(self) -> int:
        return self.health

    def get_stamina(self) -> int:
        return self.stamina

    def get_power(self) -> int:
        return self.power


@dataclass
class Predator(Creature):
    def __init__(self, max_pos=POSITION_RANGE[1]):
        predator_chars = generate_characteristics(max_position=max_pos - 1)
        super(Predator, self).__init__(predator_chars[0], predator_chars[1], predator_chars[2], predator_chars[3],
                                       predator_chars[4], predator_chars[5], predator_chars[6], predator_chars[7])


@dataclass
class Prey(Creature):
    def __init__(self):
        prey_chars = generate_characteristics(min_position=POSITION_RANGE[0] + 1)
        super(Prey, self).__init__(prey_chars[0], prey_chars[1], prey_chars[2], prey_chars[3],
                                   prey_chars[4], prey_chars[5], prey_chars[6], prey_chars[7])
