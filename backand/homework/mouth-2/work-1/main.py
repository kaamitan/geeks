class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points: int, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.fly = False

    def get_name(self):
        return self.name

    def duble_health(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points

    def __str__(self):
        return f'\nname: {self.name}\nnick_name: {self.nickname}\nsuper_power: {self.superpower}\nhealth: {self.health_points}\ncatch_phrase: {self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)

    def true_phrase(self):
        if self.fly:
            return f'True in the True_phrase'

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage


    def duble_health(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def duble_health(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points

class Villain(SuperHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def gen_x(self):
        pass

    def crit(self, target):
        return target.damage ** 2

air_hero = AirHero("Джон", "Летун", "Ветер", 150, "Я выше всех", 50)
earth_hero = EarthHero("Марк", "Земляной", "Сила земли", 200, "Я стою на земле крепко", 70)
villain = Villain("Локи", "Мастер иллюзий", "Иллюзии", 120, "Я сделаю хаос", 80)

print(air_hero.duble_health()) 
print(air_hero.true_phrase())  
print(earth_hero.duble_health())  
print(earth_hero.true_phrase())  
print(villain.crit(earth_hero))  