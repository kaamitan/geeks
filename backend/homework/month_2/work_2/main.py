from hero import SuperHero


class SuperHero:
    people = "people"

    def __init__(
        self,
        name: str,
        nickname: str,
        superpower: str,
        health_points: int,
        catch_phrase: str,
        damage: int,
    ):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catch_phrase = catch_phrase
        self.damage = damage
        self.fly = False

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the {self.catch_phrase}"

    def __str__(self):
        return (
            f"\nname: {self.name}\nnick_name: {self.nickname}\n"
            f"super_power: {self.superpower}\nhealth: {self.health_points}\n"
            f"catch_phrase: {self.catch_phrase}"
        )

    def __len__(self):
        return len(self.catch_phrase)


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catch_phrase, damage):
        super().__init__(
            name, nickname, superpower, health_points, catch_phrase, damage
        )


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catch_phrase, damage):
        super().__init__(
            name, nickname, superpower, health_points, catch_phrase, damage
        )


class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catch_phrase, damage):
        super().__init__(
            name, nickname, superpower, health_points, catch_phrase, damage
        )


class Villain(SuperHero):
    people = "monster"

    def __init__(self, name, nickname, superpower, health_points, catch_phrase, damage):
        super().__init__(
            name, nickname, superpower, health_points, catch_phrase, damage
        )

    def gen_x(self):
        pass

    def crit(self, multiplier: int):
        self.damage *= multiplier


air_hero = AirHero(
    "Skyler", "Windman", "Fly, Storm Control", 800, "I rule the skies!", 50
)
earth_hero = EarthHero(
    "Terra", "Earthquake", "Earth Manipulation", 900, "Feel the ground shake!", 70
)
space_hero = SpaceHero(
    "Galaxor", "Starshine", "Gravity Control", 1000, "I am the cosmos!", 100
)

print(air_hero)
air_hero.double_health()
print(air_hero.true_phrase())

print(earth_hero)
earth_hero.double_health()
print(earth_hero.true_phrase())

print(space_hero)
space_hero.double_health()
print(space_hero.true_phrase())

villain = Villain("Evilman", "Villainous", "Chaos Control", 500, "I am your doom!", 80)
villain.crit(2)
print(f"Damage злодея {villain.get_name()}: {villain.damage}")

air_hero.health_points -= villain.damage
print(f"Здоровье {air_hero.get_name()} после атаки злодея: {air_hero.health_points}")
