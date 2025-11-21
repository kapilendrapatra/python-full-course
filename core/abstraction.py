'''it's a processof hiding the implementation from the user by showing them only the functionalities.
it's combination of 3 sub-parts
1.abstract method
2.abstract class
3.concrete class
here to use abstract method we have to import an module called ABC and @abstractmethod
'''
from abc import ABC,abstractmethod
class Animal(ABC):   #abstract class
    @abstractmethod
    def sound(self):   #abstract method
        pass
class Dog(Animal):   #concrete class
    def sound(self):
        return "bark"
class Cat(Animal):   #concrete class
    def sound(self):
        return "meow"
dog=Dog()
cat=Cat()
print(dog.sound())
print(cat.sound())
