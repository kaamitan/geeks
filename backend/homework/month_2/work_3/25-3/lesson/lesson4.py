# множественное наследование
from lesson3 import Emirlan
class O:...
class A(O):...
class B(O):...
class C(O):...
class D(O):...
class E(O):...

class K1(A,B,C):...
class K2(B,D):...
class K3(C,D,E):...


class Z(K1,K2,K3):...

# print(Z.mro())



class One:
    def __init__(self,name):
        self.name=name

class Tho():
    # def __init__(self,age):
    #     self.age=age
    def f(self):
        print('Амир молчит')

class Tho2(One):
    def F(self):
        print('Амир говорит')


class Three(Tho2,Tho):
    # def __init__(self, name,age):
    #     Tho.__init__(self,age)
    #     Tho2.__init__(self,name)

    def __str__(self):
        return f'{self.name}'


c=Three('name')
print(c)





