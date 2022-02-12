# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Pythonforprogrammers"
        self.__c = "Python for programmers"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
        # Driver code

    obj1 = Base()
    print(obj1.a)
    # Uncommenting will
    print(obj1.c)  # raise an AttributeError
    # Uncommenting
    obj1 = Derived()  # also raise an AtrributeError as
    # private member of base class
    # is called inside derived class

'''Pythonforprogrammers
Traceback (most recent call last):
  File demeprivatemem.py", line 9, in <module>
    class Derived(Base):
  File demeprivatemem.py", line 21, in Derived
    print(obj1.c)  # raise an AttributeError
AttributeError: 'Base' object has no attribute 'c'
'''