'''it's a phenomenon of providing security to the data-members of the class.
data-members including all the properties,functionalities and methods.
it's also known as access specifiers.
it tells us till what extends we can access and modify the data members.
it's of 3 types:
1. public access specifiers
2. protected access specifiers(single underscore) it internaally works similar to public access specifiers. 
3. private access specifiers(double underscore)
'''
# public access specifiers
class A:
    def __init__(self):
        self.name = "hacker"
        self._age = 21
        self.__id = 1234
obj = A()
print(obj.name)      # public member can be accessed outside the class

# protected access specifiers
class B:
    def __init__(self):
        self._name = "hacker"
        self._age = 21
        self.__id = 1234
obj1 = B()
print(obj1._name)    # protected member can be accessed outside the class but it's not recommended

# private access specifiers
class C:
    def __init__(self):
        self.__name = "hacker"
        self.__age = 21
        self.__id = 1234
obj2 = C()
# print(obj2.__name)  # private member cannot be accessed outside the class it will raise an attribute error
# but we can access private members using 3 methods
#1.syntax method
#2.getter-setter funnction
#3.property decorator

#1.syntax method(syntax:objname._ClassName__privateMemberName)
print(obj2._C__name)  # accessing private member using syntax method
print(obj2._C__age)
print(obj2._C__id)
#2.getter-setter function
class D:
    def __init__(self):
        self.__name = "hacker"
        self.__age = 21
        self.__id = 1234
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
obj3 = D()
print(obj3.get_name())  # accessing private member using getter method
obj3.set_name("new_hacker")
print(obj3.get_name())  # accessing modified private member using getter method
#3.property decorator
class E:    
    def __init__(self):
        self.__name = "hacker"
        self.__age = 21
        self.__id = 1234
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
obj4 = E()
print(obj4.name)  # accessing private member using property decorator
obj4.name = "new_hacker"
print(obj4.name)  # accessing modified private member using property decorator

