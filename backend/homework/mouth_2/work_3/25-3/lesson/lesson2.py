# Наследование,полиморфизм

# инкапсуляция


# супер класс
class Robot:
    brain=True
    def __init__(self,name,model,color,destination):
        self.name=name
        self.model=model
        self.color=color
        self.dest=destination


    def __str__(self):
        return f'name is {self.name}\n' \
               f'color is {self.color}\n' \
               f'model is {self.model}'
    def desti(self):
        print(self.dest)

robot=Robot('Влад','А4','blue','снимать видео')
print(robot)
print(robot.desti())

# дочерний класс
class Robot2(Robot):
    brain = False
    def __init__(self,name, model, color, destination,fly):
        super().__init__(name, model, color, destination)
        Robot.__init__(self,name, model, color, destination)
        self.fly=fly
    def desti(self):
        self.fly=False
        print(self.fly)

robot2=Robot2('termonator','T1001','pink','отбирает одежду',True)
print(robot2.fly)
robot2.desti()
print(robot2.fly)

robot.desti()
robot2.desti()
print(robot2.brain,robot.brain)

class Robot3(Robot2):
    def desti(self):
        print(self,' теперь летает')


MegaTron=Robot3('TRANSformer','Desipticon','RED','WARS',False)
MegaTron.desti()


class Human:
    # атрибуты уровня класса
    head = 1
    body = 1
    hands = 2

    # метод :конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'head is {self.head}'


hum=Human('Алдияр',18)
Robot3.desti(hum.age)






#
# # инкапсуляция
# # git clone
#
# class Emirlan:
#     head=1
#     hands=2
#     foots=2
#     def __init__(self,name='Emirlan',age=18):
#         self.__name=name
#         self._age=age
#     def __str__(self):
#         return f'{self.__name} ' \
#                f'{self._age}'
#
#     def run(self):
#         self.__run()
#         self.__g()
#         print(self._age - 1)
#         print(self.__name)
#
#
#     def __run(self):
#         print(self.__name, 'run')
#
#     def __g(self):
#         pass
#
# e=Emirlan()
# e.run()
#
# print(e._age)
# e._age=11
# e._Emirlan__name='name'
# print(e._age)
# # print(e._Emirlan__name)
# e.__name='name'
# # print(dir(e))
# r='qwertyu'
# print(dir(e))
