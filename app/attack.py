from abc import abstractmethod


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
