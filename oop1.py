
# positon, name, age level, salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 20, "Senior", 7000]

# class
class SoftwareEngineer:

# class attributes
    alias = "keyboard Magician"
    
    def __init__(self, name, age, level, salary):
    # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# Instance
se1 = SoftwareEngineer("Max",20,"Junior", 5000)
print(se1.name, se1.age)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se2.alias)


# Recap
# create a class (blueprint)
# create a instance (object)
#class vs instance
#instance attributes: definied in __init__(self)
# class attribute
