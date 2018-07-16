#Static functions are normal functions
#They dont pass either class as an argument like the class functions
#Nor do they pass the instance as a =n argument like the regular methods of the class
#Still static methods are included into the class for the following reasons


class Employee:
    #Thus raise amount variable is a class variable and is common to all instances
    raise_amount = 1.04
    #Keeping track of how many employees we have
    num_employee = 0
    #We need to increase num_employee by 1 everytime a new employee is added so we will put it in init as init runs
    #everytime an object is created

    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@mobiusservices.in'
        Employee.num_employee =self.num_employee+1

    #Class variables are not instance specific
    #Class variable must be same for each instance

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)


    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    #Class methods
        #Add a decorator
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    #This is using class methods aS an alternative constructors (first init was the constructor)
    def from_string(cls,given_string):
        first,last,pay = given_string.split('-')
        return cls(first,last,pay)

    #Static Methods dont work on instance or a class:
    @staticmethod
    def is_workday(day):#Static methods dont take either class or instance as an argument so we will not pass either as an argument
        if day.weekday == 5 or day.weekday()==6:
            return False
        else:
            return True


emp1 = Employee('Vipulkumar','Yadav',500000)

emp2 = Employee('Saurabh','Tiwari',100000)


#Lets say we want a function that would take a date and return whether or not it is a workday
import datetime
new_date = datetime.date(2016,7,10)
print(Employee.is_workday(new_date))

