#Special methods are always surrounded by double underscores

#__init__ is a special method



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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    #Supoose we want to add two employees together and results shud be the total of their salaries

    def __add__(self,other):     #Overriding built_in add method
        return self.pay + other.pay


    def __len__(self):     #Overrode the len method for length of string
        return len(self.fullname())

emp1 = Employee('Vipulkumar','Yadav',500000)

emp2 = Employee('Saurabh','Tiwari',100000)

print(emp1)
#Comment repr method and print the same thing and see the difference
#After applying str method again print the same thing
#or try printing specifically
print(repr(emp1))
print(str(emp1))
print(emp1.__repr__())
print(emp1.__str__())
print(emp1+emp2)
#Comment __add__ and print same thing and see changes
#See special methods documentation for more details

print('test'.__len__())
print(len(emp1))
#Comment len method and print len('test') and see ddifference between results
