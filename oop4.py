

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 5000
        self._num_bugs_solved = 0


def code(self):
    self._num_bugs_solved +=1

# getter
def get_salary(self):
    return self._salary


#setter
def set_salary(self, value):
    #check value, enforce constrains
    self._salary = value
    if value < 1000:
        self._salary = 1000
    if value > 2000:
        self._salary = 2000
    self._salary = value    


def _calculate_salary(self, base_value):
    if self._num_bugs_solved < 10:
        return base_value
    if self._num_bugs_solved < 100:
        return base_value * 2
    return base_value * 3

se = SoftwareEngineer("Max", 25)
print(se.age, se.name)        

se.set_salary(6000)

for i in range(70):
    se.code
    print(se._num_bugs_solved)
print(se.age, se.name)

print(se.salary)


# Recap 
# encapsulation
# abstraction
# public. private
# getter setter
# 