name = 'Michael'
age = 49


def print_name_age():
    name_and_age = 'Your name is '+name+'and your age is '+str(age)
    print(name_and_age)


def print_two(val1, val2):
    """
    Gets two numbers and prints them
    """
    print(val1)
    print(val2)


def calculate_decades(val_age):
    return val_age//10


print_name_age()
print_two(25, [1, 2, 3, 'text'])
print('You lived for '+str(calculate_decades(age))+' decades')
