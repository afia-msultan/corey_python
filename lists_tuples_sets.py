courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

print(len(courses)) # length of list

print(courses[-1]) # location of an item in list - as an index starts at 0
# -1 is the last item in the list

print(courses[0:2]) # range; includes all values from the first index upto the last index
                           # but not including the last index

print(courses[:2]) # all courses up to 2 but not including 2
print(courses[2:]) # all courses from 2 and till the end


# add to list
courses.append('Gym')
print(courses)

# add item to a specific location in list
courses.insert(0, 'Art')
print(courses)

# a list within a list
courses_2 = ['Biology', 'Education']
# courses.insert(0, courses_2)
# print(courses)

# adding individual values from one list to another
courses.extend(courses_2)
print(courses)

# remove values from list
courses.remove('Math')
print(courses)

# with default, will remove last item from list
popped = courses.pop()
print(courses)
print(popped) # can also return item it removed

# reverse list
courses.reverse()
print(courses)

# sort in alphabetical order or ascending order for numbers
courses.sort()
print(courses)

nums = [1, 5, 4, 3]
nums.sort()
print(nums)

# sorting in descending order for numbers and letters
nums.sort(reverse=True)
courses.sort(reverse=True)
print(nums)
print(courses)

# sorting w/o altering original
sorted_courses = sorted(courses)
print(sorted_courses)

print(min(nums)) # returns min value
print(max(nums)) # returns max value
print(sum(nums)) # returns sum of all values

print(courses.index('CompSci')) # returns index
print('Art' in courses) # checks if value is in list

# lopping through each value of list - each time the loop is executed item is equal to the next value in list
for item in courses:
    print(item) # indented

# to get each item in list along with its index, can also start at a value other than 1 for index
for index, courses in enumerate(courses, start=1):
    print(index, courses)


courses = ['History', 'Math', 'Physics', 'CompSci']

# turning lists into comma (or any other symbol) separated values
courses_str = ', '.join(courses)
print(courses_str)

# converting the string values back into a list
new_list = courses_str.split(' - ')
print(new_list)

# ------------------------------
print("-------------------------TUPLES-------------------------------------")
# TUPLES
# we cannot modify tuples (immutable) - lists are mutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
    # this will not work since tuples are immutable - cannot mutate/modify the list
    # but can loop through a tuple

print(tuple_1)
print(tuple_2)

print("-------------------------SETS-------------------------------------")
cs_courses ={'History', 'Math', 'Physics', 'CompSci', 'Math'} # math is here twice but will only print once
print(cs_courses)

# SETS DO NOT CARE ABOUT ORDER - WILL PRINT OUT A DIFFERENT ORDER EVERYTIME

# conduct membership test
print('Math' in cs_courses)

# can detect what values they share or don't share with other sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses)) # what courses are in both sets
print(cs_courses.difference(art_courses))  # what courses are different in both sets
print(cs_courses.union(art_courses)) # all courses from both sets

# Empty lists - use either method
empty_list = []
empty_list = list()

# Empty tuples - use either method
empty_tuple = ()
empty_tuple = tuple()

# Empty sets
# empty_set = {} - this isn't right - it is a dict
empty_set = set()