def my_function():
    parameter = int(input())
    if parameter > 0:
        print(f'The number {parameter} is positive.')
    elif parameter < 0:
        print(f'The number {parameter} is negative.')
    else:
        print(f'The number 0 is zero.')



if __name__ == '__main__':
    my_function()

