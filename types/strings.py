# reference for strings

# a string can be in single quotes ' or double quotes "
string1 = 'See!'
string2 = "See!"

# two strings can be added together
string3 = 'a' + 'b'

# and even multiplied
string4 = 'ab' * 5
print(string4)

# single quotes can be used within double quotes
string5 = "That's crazy!"

#escaping is with a back slash
string6 = 'That\'s crazy!'
print(string6)

# We can even do multiline strings

bigString = """ I THINK THIS
WHOLE MULTILINE THING
IS INSANE."""

# and the multiline string can contain both quote types
bigQuotedString = """ "It's Insane,
how flexible
This language is..."
Said Branny"""
print(bigQuotedString)

# strings have LOTS of built in methods
testString = "Hello world"

#some common ones
testString.upper()
testString.lower()

# strings also work like lists
singleChar = testString[3]

# substring exists, but is called "slicing"
# mystring[start:stop:step_size]
testString[::-1]
print(testString[::-1])

# Get string length
len(testString)

# straight forward splitting with delimiter
splitString = testString.split(' ')
print(splitString) # <- this returns a python list

# default split without a param is a split around whitespace
# This will account for all forms of whitespace (space, tab, etc...)
splitString2 = testString.split()
print(splitString2)

# Replacing parts of a string
HelloWorld = 'HelloWorld'
HelloWorld.replace('World', 'Chicken')
print(HelloWorld.replace('World', 'Chicken'))

# IMPORTANT
# Interesting behaviour I have found with strings is that methods like
# "Replace" don't manipulate an existing string, just return a new one
# e.g
HelloWorld = 'HelloWorld'
HelloWorld.replace('World', 'Chicken')
print(HelloWorld)
# stil returns "HelloWorld"

# Strings + variables using f-string
hour = 12
print(f'It is {hour} o clock')

# and you can even manipulate them in place!
age = 21
print(f'I am totally {age - 4} years old')




