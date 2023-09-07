import sys

import my_module as mm                     # changing name of module to make it short
from my_module import find_index, test     # import specific functions/variables only
# from my_module import * # imports everything; is usually never used as it makes it harder to track problems

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

print(sys.path)

print('-----------------------------------------------------------------')
# ------------------------------------------------------------------------

# libraries:
courses = ['History', 'Math', 'Physics', 'CompSci']

# printing random item from list everytime
import random
random_course = random.choice(courses)
print(random_course)

# for math operations/calculations
import math
# e.g. converting degrees to radians
rads = math.radians(90)
print(math.sin(rads))

# work with dates and times
import datetime
import calendar

# print today's date
today = datetime.date.today()
print(today)

print(calendar.isleap(2020)) # checking for leap year

# access to underlying operating system
import os
print(os.getcwd())

print(os.__file__) # prints location of file where standard library can be viewed
