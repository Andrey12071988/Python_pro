# Класс принимает тип животного (название одного из созданных классов) 
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа 
# и верните его из класса-фабрики.


from DZ_10_1 import *

# pet = Dog('Bob', 5, 'Скулит')
# print(pet.name, pet.spec)

class Fabrica(Dog):
    
    def __init__(self, name, age, spec):
        super.__init__(name, age, spec)
        self.name = name
        self.age = age
        self.gav = spec
    
    p1 = Dog("Тузик", 5, "Воет")
    # p1.speed = 25


Fabrica.p1.speed = 25
print(Fabrica.p1.name, Fabrica.p1.spec, Fabrica.p1.speed)