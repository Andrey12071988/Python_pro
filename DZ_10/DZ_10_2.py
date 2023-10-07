from DZ_10_1 import Dog

# pet = Dog('Bob', 5, 'Скулит')
# print(pet.name, pet.spec)

class Fabrica(Dog):
    
    def __init__(self, name, age, spec):
        super().__init__(name, age, spec)
    
    bobic = Dog("Тузик", 3, "Воет")
    
print(Fabrica.bobic.name, Fabrica.bobic.spec)