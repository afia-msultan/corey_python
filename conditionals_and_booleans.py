# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Java'

if language == 'Python':
    print("language is Python")
elif language == 'Java':
    print("language is Java")
elif language == 'JavaScript':
    print("language is JavaScript")
else:
    print('No match')

print('-------------------------- Boolean Statements -----------------------------------')

# Boolean Statements:
# and
# or
# not

user = 'Admin'
logged_in = False

print("---------------AND--------------")

if user == "Admin" and logged_in: # both have to be True
    print("Admin Page")
else:
    print('Bad Creds')

print("---------------OR--------------")

if user == "Admin" or logged_in: # either has to be True
    print("Admin Page")
else:
    print('Bad Creds')

print("---------------NOT--------------")

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

print('-------------------------')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # a is equal to b

print(id(a))
print(id(b))
print (a is b) # but a is not b - their ids are different


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
# everything else will evaluate to True

print('---------------FALSE-----------------')

condition = False
    # could also be None, 0, '', (), [], {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# True:
condition = 10

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')