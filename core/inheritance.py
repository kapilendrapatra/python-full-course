''' inheritance means accessing the datamembers (attributes and methods) of a class from another class.
    It provides reusability of code.
    There are different types of inheritance in python:
    1. single inheritance
    2. multiple inheritance
    3. multilevel inheritance
    4. hierarchical inheritance
    5. hybrid inheritance
'''
# single inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
# multiple inheritance
class Flyable:
    def fly(self):
        return "Flying"
class Bird(Animal, Flyable):
    def chirp(self):
        return "Bird chirps"
# multilevel inheritance
class Puppy(Dog):
    def weep(self):
        return "Puppy weeps"
# hierarchical inheritance
class Cat(Animal):
    def meow(self):
        return "Cat meows"
# hybrid inheritance
class Bat(Animal, Flyable):
    def screech(self):
        return "Bat screeches"