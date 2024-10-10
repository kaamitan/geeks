class Human:
    head=1
    def __init__(self,name,age,):
        self.__name=name
        self._age=age
    def __run(self):
        print(f'{self.__name} is running')



h=Human('Азирет', 20)
print(h._Human__name)



class Human2(Human):
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name


g=Human2('Emirlan',11)
print(g.set_name('jakir'))
print(g.get_name())



class Human3:
    def __init__(self, name, age, ):
        self.__name = name
        self._age = age

    def __run(self):
        print(f'{self.__name} is running')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
l=Human3('kelli',29)
print(l.name)
l.name='Amir'
print(l.name)




