class Animal:
    def speak(self):
        print("Animal speaking")
class dog(Animal):
    def bark(self):
        print("dog barking")
class dogchild(dog):
    def eat(self):
        print("Eating bread....")
d=dogchild()
d.bark()
d.eat()
d.speak()

'''dog barking
Eating bread....
Animal speaking'''