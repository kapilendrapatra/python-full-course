''' it's a phenomenon of operators and methods to perform 2 or more functionalities.
For example, the + operator is used to add 2 numbers as well as to concatenate 2 strings.
Similarly, the len() method is used to get the length of a string as well as the length of a list.
In Python, polymorphism is implemented through method overriding and operator overloading.
method overloading is not supported in Python. instead you can use monkey patching to achieve the same functionality.
'''
# Example of polymorphism using method overriding
class demo:
    def sam():
        print("this is sam method of demo class")
    def sam(a):
        print("this is sam method of demo class with argument:", a)
    def sam(a, b):
        print("this is sam method of demo class with 2 arguments:", a, b)
demo.sam(5, 10)  # this will call the last defined sam method
# Example of polymorphism using Monkey Patching
class demo:
    def sam(self):
        print("this is sam method of demo class")
    first = sam  # assigning sam method to first
    def sam(self, a):
        print("this is sam method of demo class with argument:", a)
    second = sam  # assigning sam method to second
    def sam(self, a, b):
        print("this is sam method of demo class with 2 arguments:", a, b)
    third = sam  # assigning sam method to third
d = demo()
d.first()          # this will call the first method
d.second(5)       # this will call the second method
d.third(5, 10)    # this will call the third method
# Example of polymorphism using operator overloading
print(5 + 10)          # addition of 2 numbers
print("Hello " + "World")  # concatenation of 2 strings
# Example of polymorphism using len() method
print(len("Hello World"))  # length of string
print(len([1, 2, 3, 4, 5]))  # length of list
print(len((1, 2, 3, 4)))  # length of tuple
print(len({"a": 1, "b": 2, "c": 3}))  # length of dictionary

# Example of creating own operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # this will call the __add__ method
print(p3)  # Output: Point(6, 8)