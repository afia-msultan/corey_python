# allow us to work with key value pairs - like an actual dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])

print(student.get('phone', 'Not Found'))  # for keys that do not exist

student['phone'] = '555-5555' # add values
print(student.get('phone', 'Not Found')) # print if found otherwise return not found

student['name'] = 'Jane' # update another value
print(student)

student.update({'name': 'Bob', 'age': 26, 'phone': '555-5454'})  # update multiple values
print(student)

del student['age']  # delete a key
print(student)

# pop method: removes and returns values
courses = student.pop('courses')
print(student)
print(courses)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(len(student)) # print length of dict.
print(student.keys())  # print all keys
print(student.values())  # print all values
print(student.items()) # print keys and values as pairs

print("------------LOOP--------------------")

for key, value in student.items():  # to loop through each pair of key and value
    print(key, value)