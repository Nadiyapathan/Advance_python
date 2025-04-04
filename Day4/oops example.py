from abc import ABC,abstractmethod

#1.class & objects
class Person:
    def __init__(self,name,age):
        self.name=name #public attribute
        self.__age=age#private attribute(encapsulation)

    def display(self):
        print(f"name:{self.name},Age:{self.__age}")

    def get_age(self):  #getter for private attribute
        return self.__age


#inheritance
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)#calling parent constructor
        self.salary=salary

   #Method overriding
    def display(self):
        print(f"employee Name:{self.name},Age:{self.get_age()},Salary:{self.salary}")
  #4.abstractions(using abc module)
class Shape(ABC):

 @abstractmethod

 def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
   # 5.polymorphism   
class MathOperations:
    def add(self,a,b,c=0):

        return a+b+c
 #6.staticc method
class Utils:
    @staticmethod
    def greet():
        print("welcome to oops")
        #class method
class Company:
    company_name="Tech crop"
    @classmethod
    def set_company_name(cls,new_name):
        cls.company_name=new_name

        #testing the oop concept
        
# --- Testing the OOP Concepts ---
if __name__ == "__main__":
    # Creating Person Object
    p1 = Person("Alice", 25)
    p1.display()

    # Creating Employee Object (Inheritance + Overriding)
    emp1 = Employee("Bob", 30, 50000)
    emp1.display()

    # Using Abstraction
    c = Circle(5)
    print(f"Circle Area: {c.area()}")

    # Polymorphism (Method Overloading)
    math = MathOperations()
    print(f"Addition (2 params): {math.add(5, 10)}")
    print(f"Addition (3 params): {math.add(5, 10, 15)}")

    # Using Static Method
    Utils.greet()

    # Using Class Method
    print(f"Old Company Name: {Company.company_name}")
    Company.set_company_name("NewTech Corp")
    print(f"Updated Company Name: {Company.company_name}")       


