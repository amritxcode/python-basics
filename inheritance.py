class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print("Driving...")

car = Car("Toyota", "Fortuner")

car.start()
car.drive()
