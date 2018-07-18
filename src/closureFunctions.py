
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)

    return inner_function #removed Paranthesis


my_func = outer_function() #MY func is  = inner_function(){ready to be executed}
my_func()
my_func()
my_func()