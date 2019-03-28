import sys
import time
from abc import ABC, abstractmethod


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class PlayingField:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.__field = [[None for i in range(self.y_size)] for j in range(self.x_size)]

    def get_on_position(self, x, y):
        try:
            return self.__field[x][y]
        except Exception as e:
            sys.stderr.write(e)
            raise e

    def get_field(self):
        return self.__field

    def move(self, x_now, y_now, x_pos, y_pos):
        try:
            self.__field[x_now][y_now]
            self.__field[x_pos][y_pos]
        except Exception as e:
            sys.stderr.write(e)
            raise e

        if self.__field[x_pos][y_pos] is None and self.__field[x_now][y_now] is not None:
            self.__field[x_pos][y_pos] = self.__field[x_now][y_now]
            return True
        else:
            return False

    def place_unit(self, x_pos, y_pos, unit):
        try:
            self.__field[x_pos][y_pos]
        except Exception as e:
            sys.stderr.write(e)
            raise e

        if self.__field[x_pos][y_pos] is not None:
            return False
        else:
            self.__field[x_pos][y_pos] = unit
            return True


class Unit:
    def __init__(self):
        self.health = type(self).health
        self.attack_speed = type(self).attack_speed
        self.damage = type(self).damage
        self.armor = type(self).armor
        self.speed = type(self).speed
        self.invisibility = type(self).invisibility
        self.side = type(self).side

    def can_attack(self):
        if hasattr(self, 'last_attack'):
            if time.time() - self.last_attack < 10 / self.attack_speed:
                return False
            else:
                self.last_attack = time.time()
                return True
        else:
            self.last_attack = time.time()
            return True

    def can_move(self):
        if hasattr(self, 'last_move'):
            if time.time() - self.last_move < 1000 / self.speed:
                return False
            else:
                self.last_move = time.time()
                return True
        else:
            self.last_move = time.time()
            return True

    def attacked(self, damage):
        self.health -= int(damage * (1 - self.armor / 100))
        if self.health <= 0:
            self.die()

    def die(self):
        del self

    def __str__(self):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_cannon(self):
        pass

    @abstractmethod
    def create_scout(self):
        pass


@singleton
class DireArmyFactory(AbstractFactory):
    def create_cannon(self):
        return DireCannon()

    def create_scout(self):
        return DireScout()


@singleton
class RadiantArmyFactory(AbstractFactory):
    def create_cannon(self):
        return RadiantCannon()

    def create_scout(self):
        return RadiantScout()


class AbstractCannon(Unit):
    health = 200
    attack_speed = 3
    damage = 100
    armor = 10
    speed = 300
    invisibility = 0.05


class DireCannon(AbstractCannon):
    side = 'Dire'

    def __str__(self):
        return 'Dire cannon'


class RadiantCannon(AbstractCannon):
    side = 'Radiant'

    def __str__(self):
        return 'Radiant cannon'


class AbstractScout(Unit):
    health = 50
    attack_speed = 10
    damage = 20
    armor = 5
    speed = 800
    invisibility = 0.7


class DireScout(AbstractScout):
    side = 'Dire'

    def __str__(self):
        return 'Dire scout'


class RadiantScout(AbstractScout):
    side = 'Radiant'

    def __str__(self):
        return 'Radiant scout'


def main():
    pass


if __name__ == '__main__':
    main()
