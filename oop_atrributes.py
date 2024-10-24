class Student:
    # class variables
    school_name = 'ABC School'

    # constuctor
    def __init__(self, name, age):
        # instance variables
        self.name= name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age) 

# access class variable
print('School name:', Student.school_name)

# modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

#Modify class variables
Student.school_name= 'XYZ School'
print('School name:',Student.school_name)
    