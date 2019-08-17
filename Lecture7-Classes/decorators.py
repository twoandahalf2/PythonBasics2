#Decorator - function that takes another function as argument , adds fnctionality and returns another functionality

#original function is = to the function wrapped in the decorator


def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function


### Two statements below are exactly the same ( decorator is above)
@decorator_function
def display():
    print('display function ran')


display = decorator_function(display)