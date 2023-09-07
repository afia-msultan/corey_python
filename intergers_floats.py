# integer: whole number
# float: decimal

num = 3.14
print(type(num))

# Arithmetic Operators:
# Addition: 3 + 2
# Subtraction: 3 - 2
# Multiplication: 3 * 2
# Division: 3 / 2
# Floor Division: 3 // 2 --> no decimal
# Exponent: 3  ** 2
# Modulus: 3 % 2 --> remainder after division
    # mod 2: if remainder is 1, then odd; if remainder is 0, then even
# use parentheses for order of operations
print(3 * (2 + 1 ))  # order of operations example

num = 1
num += 1  # is the same as num = num + 1
print(num)

num *= 10
print(num)

# Absolute value
print(abs(-3))

# Round
print(round(3.75, 1))

# Comparisons:
# Equal: 3 == 2
# Not Equal: 3 != 2
# Greater than: 3 > 2
# Less than: 3 < 2
# Greater or equal: 3 >= 2
# Less or equal: 3 <= 2

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_1 = '100' # string
num_2 = '200' # string
print(num_1 + num_2) # like 'adding' strings not numbers

# turn these into integers (casting from strings to integers)
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)