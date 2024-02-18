class Person:
    contPerson=0
    def __init__(self, name, age):
        self.name=name
        self.age=age 
        Person.contPerson+=1
    # def getData(self, name, age):
    #    self.name=name
    #    self.age=age 

    def walk(self):
        print('A person can walk')
    
    def displayData(self):
        print("Id is ",Person.contPerson)
        print("Name of the person is ",self.name)
        print("Age of the person is ",self.age)

    def __del__(self):
        print("This is destructor")

obj=Person('Ranjan', 30)
obj.displayData()
obj.walk()

obj1=Person('Shyamal', 20)
obj1.displayData()
obj1.walk()

obj2=Person('Sanjana', 24)
obj2.displayData()
obj2.walk()