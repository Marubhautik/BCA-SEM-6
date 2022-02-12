class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()

'''
<function Person.greet at 0x00000000028FA488>
<bound method Person.greet of <__main__.Person object at 0x00000000027BDB70>>
Hello'''