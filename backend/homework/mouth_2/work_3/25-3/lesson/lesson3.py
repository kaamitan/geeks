# инкапсуляция
# git clone

class Emirlan:
    head=1
    hands=2
    foots=2
    def __init__(self,name='Emirlan',age=18):
        self.__name=name
        self.__age=age
    def __str__(self):
        return f'{self.__name} ' \
               f'{self.__age}'

    @property
    def emirlan(self):
        return f'{self.__name} {self.__age}'
    @emirlan.setter
    def emirlan(self,name,age):
        self.__name=name
        self.__age=age

    def run(self):
        self.__run()
        self.__g()
        print(self.__age - 1)
        print(self.__name)


    def __run(self):
        print(self.__name, 'run')

    def __g(self):
        pass



e=Emirlan()
e.run()


e._age=11
e._Emirlan__name='name'
print(e._age)
# print(e._Emirlan__name)
e.__name='name'
# print(dir(e))
r='qwertyu'
# print(dir(e))


amir=Emirlan('Emirlan',0)

print(amir.emirlan)






