li = [9,1,8,2,7,3,6,4,5]

li.sort() # method
print(li)

s_li = sorted(li) # function
print(s_li)

rs_li = sorted(li, reverse=True)
print(rs_li)

li.sort(reverse=True)
print(li)

# -------------------------------------------------------------------
print("----------------------------------------------------------------------")

tup = (9,1,8,2,7,3,6,4,5)

s_tup = sorted(tup)
print(s_tup)

# -------------------------------------------------------------------
print("----------------------------------------------------------------------")

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print(s_di) # will sort keys

# -------------------------------------------------------------------
print("----------------------------------------------------------------------")

li = [-6,-5,-4,1,2,3]

abs_li = sorted(li, key=abs)
print(abs_li)

# -------------------------------------------------------------------
print("----------------------------------------------------------------------")

from operator import attrgetter

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self): # tells python how we want this represented when it is printed out
        return '({},{},${}'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# def e_sort(emp):
#     return emp.salary # sorts by salary


s_employees = sorted(employees, key=attrgetter('salary'))
print(s_employees)
