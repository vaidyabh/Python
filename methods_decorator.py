# __str__ and __repr__ method

''' __str__ method is usually used to print the string output
    __repr__ method is used when need to have unambigious object representation
        and at the time of debugger or when to create the object representation 
    when both __str__ and __repr__ methods are called python prints the result or the __str__ method only
'''

class Student:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return ('Repr Method: Name is {} and location is {}'.format(self.name, self.location))

    def __str__(self):
        return ('Name is {} and location is {}'.format(self.name, self.location))
         

student_obj = Student('Hadoop Tech', 'IN')
print(student_obj)

# Output
'''
    Name is Hadoop Tech and location is IN
'''


#----------------Class and static methods-----------------

''' 
Static Methods 
        are defined using @staticmethod keyword, no parameter need to pass
        take the arg and process them. Can be use as utility

Class Methods
        denoted by @classmethod. Need to pass cls as the first parameter followed by args
        helpful in invoking the appropriate class as the class details are available as 1st parameter
        use when methods to be factory in class
        can access and modify the state of the class
'''


#Calling class and static methods
class classMethods:
    
    @classmethod
    def class_method(cls):
        print(f'Invoke class method of {cls}')

    @staticmethod
    def static_method():
        print('Invking static method')

#classMethods.class_method()     
#classMethods.static_method()    

# Output
    '''
     Invoke class method of <class '__main__.classMethods'>
     Invking static method
    '''

# Sample code to invoke the class and static method in the python

# import the date from datetime
from datetime import date

#Initializing the class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Defining the class method to fetch the age from the year
    @classmethod
    def stu_cls_method(cls, name, year):
        return cls(name, date.today().year - year)

    # Defining Static method
    @staticmethod
    def stu_static_method(age):
        if age > 18:
            return 'Adult'
        else:
            return 'Minor'
    
    #Convert the result to string using str method

    def __str__(self):
        return 'Student name is {} and age is {}'.format(self.name, self.age)


student1 = Student('AV', 27)
student2 = Student.stu_cls_method('AG', 1994)

print('Student1 details\n', student1)
print('Student2 details\n', student2)

# Output

''' 
Student1 details
 Student name is AV and age is 27
Student2 details
 Student name is AG and age is 26
'''