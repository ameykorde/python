# 1. make a class of car with two attributes (variables) brand and model
"""
class Car:
    def __init__(self, brand, model): # init is like a constructor
        self.brand = brand # self is this keyword # in python if we want to make connection then we have to use in another language may it happens internally but not in python
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Tata", "Safari")
print("My car brand is", my_car.brand)
print("My car model is", my_car.model)
print("My car full name is", my_car.full_name())

# 2. create an electric class which inherits from class with extra attribute battery_size
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

electric_car = ElectricCar("tesla", "Model S", "80kWh")
print(electric_car.model)
print(electric_car.battery_size)
print(electric_car.full_name())
# another_electric_car = ElectricCar("tesla", "Model S") # ERROR
"""
# 3. encapsulation : make brand attribute private (To make private add __ in start of variable name) and getter method for brand
"""
class Car:
    def __init__(self, brand, model):
        self.__brand = brand # adding two __ will make variable private
        self.model = model

    def get_brand(self):
        return f"{self.__brand}"

    def full_name(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Tata", "Safari")
# print("My car brand is", my_car.__brand) # AttributeError: 'Car' object has no attribute '__brand'
print("My car brand is", my_car.get_brand())
print("My car full name is", my_car.full_name())
"""

# 4. Polymorphism : write same method for fuel_type, for Car shows petrol or diesel and for electric show electric charge
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

    def fuel_type(self, random_string=None):
        if random_string:
            return "Checking parameter-wise polymorphism"
        return "Electric Charge"

my_car = Car("Tata", "Safari")
print(my_car.fuel_type())
electric_car = ElectricCar("tesla", "Model S", "80kWh")
print(electric_car.fuel_type()) 
print(electric_car.fuel_type("Test"))
"""


# class variable
"""
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = Car("Tata", "Safari")
electric_car = ElectricCar("tesla", "Model S", "80kWh")
print(Car.total_car)
print(my_car.total_car) 
"""

# static method
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = Car("Tata", "Safari")
electric_car = ElectricCar("tesla", "Model S", "80kWh")
print(my_car.general_description())
print(Car.general_description())
"""

# Make model variable read only
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = Car("Tata", "Safari")
electric_car = ElectricCar("tesla", "Model S", "80kWh")
# my_car.model = "City" # AttributeError: property 'model' of 'Car' object has no setter
print(my_car.model)