from abc import abstractmethod


class Movement:
    @abstractmethod
    def move(self) -> tuple[int, int]:
        """
        :return: differential of stamina and position as a tuple
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

