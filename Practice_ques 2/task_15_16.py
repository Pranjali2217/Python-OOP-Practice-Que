class vehicle:

    def __init__(self,make,model):
        self.make =make
        self.model= model


class Car(vehicle):
    def __init__(self,model,make,year):
        self.year=year
        vehicle.__init__(self,make,model)

car=Car('honda','harry',2020)
print(car.make)
print(car.model)
print(car.year)