class SuperHero():
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points: int, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def duble_health(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return f'\nname: {self.name}\nnick_name: {self.nickname}\nsuper_power:{self.superpower}\nhealth: {self.health_points}\ncatch_phrase: {self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Питер Паркер", "Человек Паук", "Путина",
                 100, "С вами ваш Дружулюбный Сосед Ч.П ")

getName = hero.get_name()
healthPoint = hero.duble_health()
lenCatphrase = len(hero)

print(hero)
