# inherits, extends, overrides
class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working..")


# SoftwareEngineer inherits from Employee
class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age)
        self.level = level
        self.salary = salary

    def work(self):
        print(f"{self.name} is coding as a {self.level} engineer..")


# Designer inherits from Employee
class Designer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print(f"{self.name} is designing..")

    def draw(self):
        print(f"{self.name} is drawing...")


# Create instances and call work method
se = SoftwareEngineer("Max", 25, 6000, "Junior")
se.work()  # This will work now

d = Designer("Philip", 27, 7000)
d.work()  # This will also work

# Polymorphism
employees = [
    SoftwareEngineer("Max", 25, 6000, "Junior"),
    SoftwareEngineer("Lisa", 30, 8000, "Senior"),
    Designer("Philip", 27, 7000)
]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

# Call the polymorphic function
motivate_employees(employees)

# Recap
# inheritance: ChildClass(baseClass)
# inherit, extend, override
# super(), __init__()
