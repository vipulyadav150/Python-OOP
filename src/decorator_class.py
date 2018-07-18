
#Using class as decorators instead of functions

class decorator_class(object):
    #How to pass original_function as argument to this class...we will use __init__ method for it

    def __init__(self,original_function):
        self.original_function = original_function
        #Above code has tied our class instance to original function method

        #How to add extra functionalities to the original function
        #We will use the __call__ method for this with *args and **Kwargs

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

@decorator_class
def display():
    print('display function ran!')


display_info("Vipulkumar",19)
display()

