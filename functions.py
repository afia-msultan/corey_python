# DRY: don't repeat yourself

def hello_func():
    return "Hello Function!"

print(hello_func().upper()) # calling/execute the function

# passing parameters
def hello_func_2(greeting, name = "You"): # greeting is a local variable; if no name is provided will return "You"
    return'{}, {}.'.format(greeting, name)

print(hello_func_2("Hi"))
print(hello_func_2("Hi", name = "Afia"))

def student_info(*args, **kwargs): # these names are conventions commonaly used; used to accept arbitrary # of values
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age' : 22}

student_info(*courses, **info) # stars used to unpack values from list/dictionary

# -----------------------------------------------------------------------------------

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2020, 2))