#About the property decorator-Tutorials Corey Schafer

class Employee:
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + '.' + last.lower() + '@mobiusservices.in'

    #add email()
    @property
    def email(self):
        return '{}.{}@mobiusservices.in'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):    #name is the value we are trying to set(fullname)
        first , last = name.split(' ')
        self.first=first
        self.last=last
        #Now this starts working print the fullname and all and check also check direct assign error solved

        #We can also make a dletor in same way

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first=None
        self.last=None



emp1 = Employee('Vipulkumar','Yadav',500000)
emp2 = Employee('Saurabh','Tiwari',100000)
# emp1.first='Jim'
emp1.fullname = 'Vipul Yadav' #error cant set attribute
#in order to run above line sucessfully we need to use setter property
#We want that as setting this fullname we want to auto change the first and last name and email

print(emp1.first)
# print(emp1.email)
# print(emp1.email())
print(emp1.email)
# print(emp1.fullname())
print(emp1.fullname)
#After adding deleter run below
del emp1.fullname
print(emp1.fullname)