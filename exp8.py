'''class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m = Manager(101, "Rahul", 50000, "IT")
m.display_manager()'''



'''class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

        discount = self.price * 0.10
        discounted_price = self.price - discount

        print("Discounted Price:", discounted_price)


c = Car("Toyota", "Innova", "Diesel", 2000000)
c.display_car()'''



'''class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        total = self.marks + self.points

        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", total)


s = Student(85, 10)
s.performance()'''


'''class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e = Employee("Priya", 22, 101, "Developer", 40000)
e.display()'''


'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)


r = ResearchStudent(
    "Aditi", 21, 25, "Computer Science",
    "Artificial Intelligence", "Dr. Sharma"
)

r.display()'''

'''class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display_details(self):
        self.display()
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


p = PremiumSavingsAccount(101, 50000, 5, "Free ATM and Insurance")
p.display_details()'''



'''import math

class Shape:
    def display(self):
        print("This is a shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

c.display()
print("Circle Area:", c.area())

r.display()
print("Rectangle Area:", r.area())

t.display()
print("Triangle Area:", t.area())'''


'''class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.salary)


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 8000


class Tester(Employee):
    def calculate_salary(self):
        return self.salary + 5000


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Priya", 35000)

m.display()
print("Manager Salary:", m.calculate_salary())

print()

d.display()
print("Developer Salary:", d.calculate_salary())

print()

t.display()
print("Tester Salary:", t.calculate_salary())'''

'''class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.salary)


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 8000


class Tester(Employee):
    def calculate_salary(self):
        return self.salary + 5000


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Priya", 35000)

m.display()
print("Manager Salary:", m.calculate_salary())

print()

d.display()
print("Developer Salary:", d.calculate_salary())

print()

t.display()
print("Tester Salary:", t.calculate_salary())'''


'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Aditi", 21, 25, "Python")
ta.display()'''


'''class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def car_details(self):
        print("Car Model:", self.model)


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def bike_details(self):
        print("Bike Model:", self.model)


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def sports_details(self):
        self.display()
        self.car_details()
        print("Top Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def electric_details(self):
        self.display()
        self.bike_details()
        print("Battery:", self.battery, "kWh")


s = SportsCar("BMW", "M4", 280)
e = ElectricBike("Ola", "S1", 4)

print("Sports Car Details:")
s.sports_details()

print()

print("Electric Bike Details:")
e.electric_details()'''


