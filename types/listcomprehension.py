# reference for list comprehensions

# list comprehensions are touted as a standout feature for python
# basically creates lists based on lists - but with cool uses

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

# <expression> can be any valid python expression
# this means listcomprehensions can be used
# very useful for making matrix's

m = [[j for j in range(5)] for i in range(6)]
print(m)

# flattening the matrix

f = [value for sublist in m for value in sublist]
print (f)

# There are alternatives to comprehensions, like map() and reduce()
# but screw that because these are beautiful

# set comprehensions
# use {} instead of []

se = {s for s in range(1, 5) if s % 2}
print(se)


# Dictionary comprehension
# requires a key and a value
# key and value both defined in the expression
d = { x: x**2 for x in (2, 4, 6)}
print(d)


