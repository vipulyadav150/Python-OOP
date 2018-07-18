
# def decorator_function(message):
#     def wrapper_function():
#         print(message)
#
#     return wrapper_function
#
#
# Hi_func = outer_function('Hi') #MY func is  = inner_function(){ready to be executed}
# Bye_func = outer_function('Bye')
# Hi_func()
# Bye_func()


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

    #So basically decorators are those that take a function as input and add some extra lines of code
    #or execute some extra lines or add some extra functionalities to existing original function
    #anad then return the function without actually modifying the code of the original function

# def display():
#     print('Display Function Ran!')

# decorated_display = decorator_function(display)#Returns wrapper fuction ready to be executed
# #decorated_display variable is equal to wrapper function ready to be executed
# decorated_display()

#now if we use
@decorator_function
#above line is equal to the following line
# display = decorator_function(display)
def display():
    print('Display Function Ran!')

#now if we call display it will give the modified ones also
display()
#So the wrapper code is added to original function


