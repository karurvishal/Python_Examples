class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0
    def get_name(self):
        info = f"{self.make} {self.model} {self.year}"
        return info.title()
    def read_odometer(self):
        print(f"the car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("cannot roll back")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self,size=75):
        self.size = size
    def describe_battery(self):
        print(f"the battery size is {self.size}")
    def upgrade_battery(self):
        if self.size != 100:
            self.size = 100
    def get_range(self):
        if self.size == 75:
            range = 260
        elif self.size == 100:
            range = 315
        print(f"this car can go about {range} miles ")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
#just to crate a branch







