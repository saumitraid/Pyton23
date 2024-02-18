class Animal:           #Base Class
    def eat(self):
        print("Eating......")

class Dog(Animal):        #Child Class
    def bark(self):
        print("Barking.......")

class Puppies(Dog):
    def weap(self):
        print('Weaping.......')
    
    def eat(self):
        print('Drink milk')

obj=Puppies()
obj.eat()
obj.bark()
obj.weap()

ob=Animal()
ob.eat()