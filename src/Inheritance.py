

class Employee:
    raise_amount = 1.04
    num_employee = 0
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@mobiusservices.in'
        Employee.num_employee =self.num_employee+1

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod

    def from_string(cls,given_string):
        first,last,pay = given_string.split('-')
        return cls(first,last,pay)


    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday()==6:
            return False
        else:
            return True

class Developer(Employee):
    raise_amount = 3.4 #Tochange raise_amount from developer class

    def __init__(self,first,last,pay,prog_lang):
        self.prog_lan = prog_lang
        super().__init__(first,last,pay)
        #Alternative to above line
        #Employee.__init__(self,first,last,pay)


class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def dispatch_emp(self):
        for employee in self.employees:
            print('---->'+employee.fullname())










# dev1 = Employee('Vipulkumar','Yadav',500000)
# dev2 = Employee('Saurabh','Tiwari',100000)

dev1 = Developer('Vipulkumar','Yadav',500000,'Python')
dev2 = Developer('Saurabh','Tiwari',100000,'Java')

#Suppose we want to be more specific that whether the employee is developer or manager
#Like both developer and manager will have the same attributes name , email , pay etc...
#So instead of copying same code in developers and managers classes we can just reuse this code by creating the subclasses

# print(dev1.email)
# print(dev2.email)
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print(dev1.prog_lan)
print('\n')
print(dev2.pay)
dev2.apply_raise()
print(dev2.pay)
print(dev2.prog_lan)
# print(help(Developer))#Print this for overview

man1 = Manager('Saurav','Saha',340000,[dev1,dev2])
dev3=Manager('Sahu','Raghu',4500)
man1.add_emp(dev3)
print(man1.fullname())
print(man1.dispatch_emp())
man1.dispatch_emp()
man1.remove_emp(dev2)
man1.dispatch_emp()

#Use these functions to test the instances and their classes
print(isinstance(man1,Developer))
print(isinstance(man1,Manager))
print(isinstance(man1,Employee))

#isSubclass
#Use this to check which classes are subclasses of what parents
print(issubclass(Developer,Manager))
print(issubclass(Developer,Employee))
