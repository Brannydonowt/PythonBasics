# Reference for loops in python

#example for-loop
for letter in 'Hello World':
    print(letter)

#lists
# lists work very different in python
# a list can have multiple types of objects
# e.g

egList = [1, 'a', 'Hello']
for item in egList:
    print(item)

# accessed like a conventional list
print(egList[0])

# You can even contain lists in lists
deepList = [1, 2, 'Look', ['Deep List 0', 'Deep List 1']]
print (deepList[3][1])

#example while list
i = 1
while i <= 4:
    print(i)
    i = i + 1

# notice there is no ++ or --

# You can use CTRL + C to break out of a while loop

