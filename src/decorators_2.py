

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        #When we were passing arguments to display_info() and it was wrapped under decorator_functiom
        #It throws errors that wrapper function shud not contain arguments
        #To add arguments to wrapper function we  shud use *args and **kwargs
        #That also will run OK with wrapper function with no arguments

        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
#above line is equal to the following line
# display = decorator_function(display)
def display():
    print('Display Function Ran!')

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))



display_info('Vipulkumar',19)
display()


