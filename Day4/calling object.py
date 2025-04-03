#car example
class Car:

    def __init__(self,make,model,year,mileage=0):
      self.make= make
      self.model= model
      self.year=year
      self.mileage=mileage

    def display_info(self):
       print(f"car Details:{self.year}{self.model}{self.mileage}{self.make}")

    def drive(self,miles):
       self.mileage+=miles
       print(f"driving{miles}miles.New mileage:{self.mileage} miles")
    def service(self):
       print(f"servicing the{self.make}{self.model}.")
       self.mileage=0
my_Car=Car("kia","seltos",2022)

my_Car.display_info()

my_Car.drive(200)

my_Car.display_info()

my_Car.service()

my_Car.display_info()          