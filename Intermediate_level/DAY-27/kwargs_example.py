def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    
calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        
        
car = Car(make="Nissan", model="GT-R")
print(car.make, car.model, car.color, car.seats)