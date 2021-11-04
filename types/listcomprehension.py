# reference for list comprehensions

# list comprehensions are touted as a standout feature for python

# basic syntax
# <expression> for item in list if <conditional>
# if <conditional> is optional

myList = [x for x in range(1, 5)]
print(myList)

# prints 1, 2, 3, 4

#with if statement
myIfList = [x for x in range(1, 10) if x % 2 == 0]
print(myIfList)

# prints numbers divisible by 2 between 1->10

# this gets quite interesting with functions

def square_and_half_number(a):
    return (a * a) / 2

l = [square_and_half_number(i) for i in range(10)]
print (l)

# We can quickly perform expressions over members of lists
# this is insane 




