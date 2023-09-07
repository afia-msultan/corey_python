nums = [1, 2, 3, 4, 5]

print('-------------------BREAK--------------------------------------')

for num in nums: # looping through list above
    if num == 3: # break the loop when num is 3
        print("Found!")
        break
    print(num)

print('-------------------CONTINUE--------------------------------------')

for num in nums: # looping through list above
    if num == 3: # skip this number the loop when num is 3
        print("Found!") # instead print this
        continue # and then continue with the rest of the numbers
    print(num)

print('-------------------------NESTED LOOPS--------------------------------')

for num in nums:
    for letter in 'abc': # loop within a loop
        print(num, letter) # prints each letter with each number

print('-------------------------RANGE--------------------------------------')

for i in range(1, 11): # starts at first passed valye and up to but not including second passed #
    print(i) # will print #s 1-10

print('-------------------------WHILE------------------------------------')

x = 0 # x starts at 0

while x < 10: # will loop until x is less than 10
    print(x) # if condition is met x is printed
    x += 1 # moves to the next #
    # can also implement break and continue within while loop (esp. with infinite loop)


print('----------------------------------------------------------------')

x = 0

while True:
    if x == 11:
        break
    print(x)
    x += 1
