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



emp1 = Employee('Vipulkumar','Yadav',500000)
emp1.num_employee = Employee.num_employee
emp2 = Employee('Saurabh','Tiwari',100000)
emp2.num_employee = Employee.num_employee
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(Employee.__dict__)
myList = [emp1,emp2]


Employee.set_raise_amount(5.6) #is the same thing as EMployee.raise_amount = 5.6
#We can run this class method from instance also as shown below
# emp1.set_raise_amount(7.8)



#Change in raise_amount(A class variable) using class
# Employee.raise_amount=1.05

#Change in raise_amount(A class variable) using instances
# emp1.raise_amount = 1.05

for x in myList:
    print('Employee number : '+str(x.num_employee))
    print(x.fullname())
    print(x.email)
    print(x.pay)
    print('Amount raise this year : '+str(x.raise_amount))
    x.apply_raise()
    print(x.pay)
    print('\n')


print(Employee.num_employee)
print(emp1.__dict__)
print(emp2.__dict__)
#Employee.fullname(emp1)
#Employee.raise_amount(This way also we can access class variables)
#emp1.raise_amount(This way also we can check of class variables)


# #Creating employees using class method
# emp3 = 'Yatharth-Mishra-200000'
# emp4 = 'Abhishek-Alwani-100000'
#
# first,last,pay = emp3.split('-')
# new_emp3 = Employee(first,last,pay)
#
# print(new_emp3.first +' '+ new_emp3.last)
# print(new_emp3.email)
# print(new_emp3.pay)

#Alternative to above code
emp3 = 'Yatharth-Mishra-200000'
emp4 = 'Abhishek-Alwani-100000'

new_emp3 = Employee.from_string(emp3)
print(new_emp3.fullname())
print(new_emp3.email)
print(new_emp3.pay)

print(Employee.num_employee)

