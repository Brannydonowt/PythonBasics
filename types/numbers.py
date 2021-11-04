#reference for numbers

# - A # is used for comments

# No need to define a type. it is context/cast driven it seems
integerExample = 4
stringExample = '3'
floatExample = 4.2

# an int in python is very very big, more than conventional language
# only limited by memory
bigInt = 12314164512424534314

# convert string to int
stringToInt = int('5')

#convert int to string
intToString = str(100)

#convert float to int
#seems to just chop off the decimal
floatToInt = int(100.9)
print(floatToInt)

#random integers
import random
randInt = random.randint(0, 100)
print('Rand Int: ' + str(randInt))

# Output var type
print(type(2))

# when using a type as a bool
if isinstance(2, int):
    print ('This is an int')
else:
    print('this is not an int')