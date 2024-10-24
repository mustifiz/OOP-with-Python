class SoftwareEngineer:

    # class attributes
    alias = "keyboard Magician"
    
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code ..")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language} ..")

    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"      
        return information

    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"    
        return information
  
    # dunder method for equality comparison
    def __eq__(self, other):
        if isinstance(other, SoftwareEngineer):
            return self.name == other.name and self.age == other.age
        return False

    # static method
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# Instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
se3 = SoftwareEngineer("Lisa", 25, "Senior", 7000)

se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

# Equality check
print(se2 == se3)  # This should now return True

# Call static method without needing an instance
print(SoftwareEngineer.entry_salary(27))  

# Recap
#instance methods(self)
# can take argumetns and return values
# special "dunder" method (__str__ and __eg__)
# @staticmethods
