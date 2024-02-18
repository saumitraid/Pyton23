class Animal:           #Base Class
    def eat(self):
        print("Eating......")

class Dog(Animal):        #Child Class
    def bark(self):
        print("Barking.......")

obj=Dog()
obj.eat()
obj.bark()