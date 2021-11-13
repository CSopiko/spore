from random import randint
from abc import abstractmethod

from dataclasses import dataclass


LEGS = 'legs'
WINGS = 'wings'
NO_LIMB = 'no_limb'

CLAWS = 'claws'
SMALL = 'small'
MEDIUM = 'medium'
BIG = 'big'
CLAWS_TYPES = {SMALL: 0, MEDIUM: 1, BIG: 2}

TEETH = 'teeth'
BLUNT = 'blunt'
SHARP = 'sharp'
SUPER_SHARP = 'super_sharp'
TEETH_TYPES = {BLUNT: 0, SHARP: 1, SUPER_SHARP: 2}

LIMBS = {LEGS: 0, WINGS: 1,  CLAWS: 2, TEETH: 3}

POWER_RANGE = [1, 3]
POSITION_RANGE = [0, 100]
HEALTH_RANGE = [0, 100]
STAMINA_RANGE = [0, 100]


@dataclass
class Creature:
    # position: int
    # power: int = 1
    # health: int = 100
    # stamina: int = 100

    def __init__(self):
        self.power = randint(POWER_RANGE[0], POWER_RANGE[1])
        self.health = randint(HEALTH_RANGE[0], HEALTH_RANGE[1])
        self.stamina = randint(STAMINA_RANGE[0], STAMINA_RANGE[1])
        self.position = randint(POSITION_RANGE[0], POSITION_RANGE[1])

    def limbs(self) -> dict:
        pass

    def generate_characteristics(self) -> None:
        pass


class Attack:
    @abstractmethod
    def attack(self, default_power) -> int:
        """

        :param default_power: creatures default damage
        :return: differential of opponents health
        """
        pass

    def __call__(self, default_power) -> int:
        return self.attack(default_power)


class DefaultAttack(Attack):
    def attack(self, default_power) -> int:
        return -default_power


class SmallClawsAttack(Attack):
    multiply_by: int = 2

    def attack(self, default_power: int) -> int:
        return - self.multiply_by*default_power


class MediumClawsAttack(Attack):
    multiply_by: int = 3

    def attack(self, default_power: int) -> int:
        return - self.multiply_by*default_power


class BigClawsAttack(Attack):
    multiply_by: int = 4

    def attack(self, default_power: int) -> int:
        return - self.multiply_by*default_power


class BluntTeethAttack(Attack):
    add_power: int = 3

    def attack(self, default_power: int) -> int:
        return - (self.add_power + default_power)


class SharpTeethAttack(Attack):
    add_power: int = 6

    def attack(self, default_power: int) -> int:
        return - (self.add_power + default_power)


class SuperSharpTeethAttack(Attack):
    add_power: int = 9

    def attack(self, default_power: int) -> int:
        return - (self.add_power + default_power)


class Movement:
    @abstractmethod
    def move(self) -> tuple[int, int]:
        """
        :return: differential of stamina and location as a tuple
        """
        pass

    def __call__(self) -> tuple[int, int]:
        return self.move()


class FlyingMovement(Movement):
    require_stamina: int = 80
    use_stamina: int = 4
    speed: int = 8

    def move(self) -> tuple[int, int]:
        return -self.use_stamina, self.speed


class RunningMovement(Movement):
    require_stamina: int = 60
    use_stamina: int = 4
    speed: int = 6

    def move(self) -> tuple[int, int]:
        return -self.use_stamina, self.speed


class WalkingMovement(Movement):
    require_stamina: int = 40
    use_stamina: int = 2
    speed: int = 4

    def move(self) -> tuple[int, int]:
        return -self.use_stamina, self.speed


class HoppingMovement(Movement):
    require_stamina: int = 20
    use_stamina: int = 2
    speed: int = 3

    def move(self) -> tuple[int, int]:
        return -self.use_stamina, self.speed


class CrawlingMovement(Movement):
    require_stamina: int = 0
    use_stamina: int = 1
    speed: int = 1

    def move(self) -> tuple[int, int]:
        return -self.use_stamina, self.speed


# {limb_type: {minimum_amount: [types of movement]}}
MOVEMENTS = {LEGS: {1: [HoppingMovement], 2: [WalkingMovement, RunningMovement]},
             WINGS: {2: [FlyingMovement]}, NO_LIMB: {0: [CrawlingMovement]}}

# {limb_type: {type: [types of attack]}}
ATTACKS = {CLAWS: {CLAWS_TYPES[SMALL]: [SmallClawsAttack],
                   CLAWS_TYPES[MEDIUM]: [MediumClawsAttack],
                   CLAWS_TYPES[BIG]: [BigClawsAttack]},
           TEETH: {TEETH_TYPES[BLUNT]: [BluntTeethAttack],
                   TEETH_TYPES[SHARP]: [SharpTeethAttack],
                   TEETH_TYPES[SUPER_SHARP]: [SuperSharpTeethAttack]}}


@dataclass
class Predator(Creature):
    def __init__(self):
        super(Predator, self).__init__()


@dataclass
class Prey(Creature):
    def __init__(self):
        super(Prey, self).__init__()
