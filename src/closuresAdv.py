#Add arguments to function and check
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function #removed Paranthesis


Hi_func = outer_function('Hi') #MY func is  = inner_function(){ready to be executed}
Bye_func = outer_function('Bye')
Hi_func()
Bye_func()