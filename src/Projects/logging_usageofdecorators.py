#Logging Problem
#Keeping track of how many times a function is run and what arguments were passed to it


from functools import wraps



def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)
    @wraps(original_function)
    def wrapper_function(*args,**kwargs):
        print('Ran with args : {} and kwargs : {}'.format(args,kwargs))
        logging.INFO('Ran with args : {} ,and kwargs : {}'.format(args,kwargs))
        return original_function(*args,**kwargs)
    return wrapper_function


def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = original_function(*args,**kwargs)
        t2 = time.time()
        run_time = t2-t1
        print('{} function ran in {} seconds'.format(original_function.__name__,run_time))
        return original_function
    return wrapper




# @my_logger
# def display_info(name,age):
#     print('display_info ran with arguments ({},{})'.format(name,age))


import time

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)#TO set delay so that we get some results otherwise it will run fast and give 0.00 sec
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('Vipulkumar',19)

#Change stack arrangement of the decorators and see the difference


