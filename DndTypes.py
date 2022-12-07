instances = {}


class StandardAttack(object):
    def __init__(self, state, damage, name, cost):
        self.unlocked = state
        self.damage = damage
        self.name = name
        self.cost = cost


class LightAttack(StandardAttack):
    def __init__(self):
        super().__init__(False, 500, "Claidheamh Soluis", 500) # super classes :) for super fun


class BowAttack(StandardAttack):
    def __init__(self):
        super().__init__(False, 8, "Bow And Arrow", 20)


class ZweiAttack(StandardAttack):
    def __init__(self):
        super().__init__(False, 30, "claidheamh mòr", 50)


class ShortAttack(StandardAttack):
    def __init__(self):
        super().__init__(True, 5, "short sword", 0)


class SpecialAttack(object): # ran out of time so i never got the chance to implement the special attacks.
    def __init__(self, state, damage, mana):
        self.unlocked = state
        self.damage = damage
        self.mana = mana


class MellowDivision(SpecialAttack):
    def __init__(self):
        super().__init__(False, 50, 60)


# noinspection NonAsciiCharacters
class MrCoileáin(SpecialAttack):
    def __init__(self):
        super().__init__(False, 100, 130)


class SunBurst(SpecialAttack):
    def __init__(self):
        super().__init__(False, 10, 30)


class Ladies(SpecialAttack):
    def __init__(self):
        super().__init__(False, 30, 40)


class Volunteers(SpecialAttack):
    def __init__(self):
        super().__init__(False, 80, 80)


class Monster(object):
    def __init__(self, name, health, max_health, strength, luck):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.luck = luck


class Monster1(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster2(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster3(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster4(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster5(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster6(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster7(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster8(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster9(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Monster10(Monster):
    def __init__(self, name, health, max_health, strength, luck):
        super().__init__(name, health, max_health, strength, luck)


class Player(object):
    def __init__(self):
        self.cash = 0
        self.health = 100
        self.level = 1  # The level in game


def load_monsters():
    for line in open("monsters.txt"):
        if line.startswith("#"):
            continue
        split = line.split(";")
        clazz = globals()[split[0]]
        instances[clazz] = clazz(split[1], split[2], split[3], split[4], split[5])
