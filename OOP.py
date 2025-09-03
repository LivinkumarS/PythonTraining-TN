class Car:
    def __init__(self,name):
        self.name=name
    
    def printWheels(self):
        print(4)
    
    def printSeats(self):
        print(7)
        
    def printName(self):
        print(self.name)
        
class Cat(Car):
    def __init__(self,name, age):
        self.name=name
        self.age=age
    
    def legs(self):
        print(4)
    
    def eyes(self):
        print(2)
        
    def printName(self):
        print(self.name)
        

    
    

car1=Car("Audi")
car2=Car("Benz")
cat1=Cat("Tom",5)

cat1.