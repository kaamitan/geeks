class SuperHero:
    people = 'people'

    def init(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def str(self):
        return f"{self.nickname}: Superpower = {self.superpower}, Health = {self.health_points}"

    def len(self):
        return len(self.catchphrase)


hero = SuperHero("Clark Kent", "Superman", "Flight", 100, "I am here to save the day!")

print(f"All heroes are {SuperHero.people}")
print(hero.get_name())
print(hero.health_points)
hero.double_health()
print(hero.health_points)
print(hero)
print(len(hero))