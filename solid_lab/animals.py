class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Chicken(Animal):
    def make_sound(self):
        return 'cluck'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())
