class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None
    
    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec="Гавкает"):
        super().__init__(name, age)
        self.spec = spec

class Cat(Animal):
    def __init__(self, name, age, spec="Мурлыкает"):
        super().__init__(name, age)
        self.spec = spec
        
class Bird(Animal):
    def __init__(self, name, age, spec="Чирикает"):
        super().__init__(name, age)
        self.spec = spec
        
# pet1 = Dog('Bob', 5, 'Гавкает')
# pet2 = Cat('Felix', 2, 'Мурлыкает')
# pet3 = Bird('Aro', 1, 'Чирикает')

# print(pet1.name, pet1.spec)
# print(pet2.name, pet2.spec)
# print(pet3.name, pet3.spec)